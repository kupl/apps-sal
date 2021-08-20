import copy
import sys
sys.setrecursionlimit(10 ** 9)


def dfs(G, v, p, d, depth):
    depth[v] = d
    for nv in G[v]:
        if nv == p:
            continue
        dfs(G, nv, v, d + 1, depth)
    return (G, depth)


(n, T, A) = map(int, input().split())
(T, A) = (T - 1, A - 1)
g = [[] for _ in range(n)]
for i in range(n - 1):
    (x, y) = map(int, input().split())
    (x, y) = (x - 1, y - 1)
    g[x].append(y)
    g[y].append(x)
depth = [0] * n
GT = copy.deepcopy(g)
GT[T].append(-1)
(GT, dt) = dfs(GT, T, -1, 0, depth)
depth = [0] * n
GA = copy.deepcopy(g)
GA[A].append(-1)
(GA, da) = dfs(GA, A, -1, 0, depth)
ans = 0
for (t, a) in zip(dt, da):
    if t <= a:
        ans = max(ans, a)
print(ans - 1)
