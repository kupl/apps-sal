import sys
sys.setrecursionlimit(10 ** 6)
(n, g, s) = map(int, input().split())
G = [[] for _ in range(n)]
for i in range(n - 1):
    (a, b) = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)


def dfs(V, v, d):
    if V[v] != -1:
        return
    V[v] = d
    for nv in G[v]:
        dfs(V, nv, d + 1)


if len(G[g - 1]) == 1 and G[g - 1][0] == s - 1:
    print(0)
else:
    vs = [-1] * n
    vg = [-1] * n
    dfs(vs, s - 1, 0)
    dfs(vg, g - 1, 0)
    ans = 0
    for i in range(n):
        if vs[i] > vg[i]:
            ans = max(ans, vs[i])
    print(ans - 1)
