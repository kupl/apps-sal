import sys
from collections import deque


def shave(fwd_link, bwd_link):
    # Vertices having no leaving link
    q = [v for v, links in enumerate(fwd_link) if not links]
    while q:
        v = q.pop()
        for u in bwd_link[v]:
            fwd_link[u].remove(v)
            if not fwd_link[u]:
                q.append(u)
    # Vertices having no entering link
    q = [v for v, links in enumerate(bwd_link) if not links]
    while q:
        v = q.pop()
        for u in fwd_link[v]:
            bwd_link[u].remove(v)
            if not bwd_link[u]:
                q.append(u)


def bfs(s, fwd_link):
    predecessors = [-1] * n
    q = deque()
    for v in fwd_link[s]:
        predecessors[v] = s
        q.append((v, s))
    visited = set()
    while q:
        v, p = q.popleft()
        if v in visited:
            continue
        visited.add(v)
        predecessors[v] = p

        if v == s:
            break

        for u in fwd_link[v]:
            if u not in visited:
                q.append((u, v))

    circuit = {s}
    v = predecessors[s]
    while v != s:
        circuit.add(v)
        v = predecessors[v]

    return predecessors, circuit


def check(predecessors, circuit, fwd_link):
    for v in circuit:
        fwd_link[v].intersection_update(circuit)
        if len(fwd_link[v]) == 1:
            continue
        for u in fwd_link[v]:
            if predecessors[u] != v:
                return u
    return -1


def print_ans(circuit):
    print((len(circuit)))
    print((*(v + 1 for v in circuit)))


def solve(fwd_link, bwd_link):
    shave(fwd_link, bwd_link)
    s = -1
    for s, (f, b) in enumerate(zip(fwd_link, bwd_link)):
        if f and b:
            break
    else:
        print((-1))
        return

    while True:
        predecessors, circuit = bfs(s, fwd_link)
        res = check(predecessors, circuit, fwd_link)
        if res == -1:
            print_ans(circuit)
            break
        s = res


n, m = list(map(int, input().split()))
fwd_link = [set() for _ in range(n)]
bwd_link = [set() for _ in range(n)]
for line in sys.stdin:
    a, b = list(map(int, line.split()))
    a -= 1
    b -= 1
    fwd_link[a].add(b)
    bwd_link[b].add(a)

solve(fwd_link, bwd_link)

