from collections import deque

n, m = list(map(int, input().split()))
deg = [0] * (n + 1)
G = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = list(map(int, input().split()))
    deg[u] += 1
    deg[v] += 1
    G[u].append(v)
    G[v].append(u)

C = [0] * (n + 1)


def dfs(v, cc):
    ok = True
    q = [v]
    C[v] = cc
    sz = 1
    while q:
        v = q.pop()
        if len(G[v]) != 2:
            ok = False
        for w in G[v]:
            if C[w] == 0:
                C[w] = cc
                sz += 1
                q.append(w)
    return sz, ok


cc = 0
cycles = 0
for v in range(1, n + 1):
    if C[v] == 0:
        cc += 1
        sz, ok = dfs(v, cc)
        if ok and sz > 2:
            cycles += 1

print(cycles)
