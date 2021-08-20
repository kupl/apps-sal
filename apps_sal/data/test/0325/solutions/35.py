from collections import deque


def use_path(n, start, es):
    q = deque()
    chk = [False] * n
    q.append(start)
    chk[start] = True
    used = {start}
    while len(q) > 0:
        node = q.popleft()
        for nex in es[node]:
            if not chk[nex]:
                chk[nex] = True
                q.append(nex)
                used.add(nex)
    return used


def belman(s, g, n, es):
    d = [10 ** 10] * n
    d[s] = 0
    fin = False
    cnt = 0
    while True:
        update = False
        for (p, q, r) in es:
            if d[p] != 10 ** 10 and d[q] > d[p] + r:
                d[q] = d[p] + r
                update = True
        cnt += 1
        if not update:
            fin = True
            break
        if cnt > n + 1:
            break
    if fin:
        return max(0, -d[g])
    else:
        return -1


(n, m, p) = list(map(int, input().split()))
l = [[] for i in range(n)]
r = [[] for i in range(n)]
edges = []
for i in range(m):
    (a, b, c) = list(map(int, input().split()))
    a -= 1
    b -= 1
    l[a].append(b)
    r[b].append(a)
    edges.append((a, b, -c + p))
use_nodes = use_path(n, 0, l) & use_path(n, n - 1, r)
es = [(a, b, c) for (a, b, c) in edges if a in use_nodes and b in use_nodes]
print(belman(0, n - 1, n, es))
