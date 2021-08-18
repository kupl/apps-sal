import sys


def find_cycle(g):
    n = len(g)
    used = [0] * n
    for v in range(n):
        if used[v] == 2:
            continue
        stack = [v]
        hist = []
        while stack:
            v = stack[-1]
            if used[v] == 1:
                used[v] = 2
                stack.pop()
                hist.pop()
                continue
            hist.append(v)
            used[v] = 1
            for c in g[v]:
                if used[c] == 2:
                    continue
                elif used[c] == 1:
                    return hist[hist.index(c):]
                else:
                    stack.append(c)
    return None


def find_minimal_cycle(g, cycle):
    n = len(g)
    is_in_cycle = [0] * n
    nxt = [-1] * n

    l = len(cycle)
    for i, c in enumerate(cycle):
        is_in_cycle[c] = 1
        nxt[c] = cycle[i + 1 - l]

    for v in cycle:
        if is_in_cycle[v]:
            for c in g[v]:
                if is_in_cycle[c] == 1:
                    v0 = nxt[v]
                    while v0 != c:
                        is_in_cycle[v0] = 0
                        v0 = nxt[v0]
                    nxt[v] = c

    i = is_in_cycle.index(1)
    v = nxt[i]
    hist = [i]
    while v != i:
        hist.append(v)
        v = nxt[v]
    return hist


sys.setrecursionlimit(10**6)
readline = sys.stdin.readline

n, m = [int(i) for i in readline().split()]
g = [[] for _ in range(n)]

for _ in range(m):
    a, b = [int(i) - 1 for i in readline().split()]
    g[a].append(b)

cycle = find_cycle(g)

if cycle == None:
    print((-1))
else:
    res = find_minimal_cycle(g, cycle)
    print((len(res)))
    for i in res:
        print((i + 1))
