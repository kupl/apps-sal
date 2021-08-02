import sys
sys.setrecursionlimit(10**9)

N = int(input())
G = [[] for _ in range(N)]
length = {}
for _ in range(N - 1):
    a, b, c = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)
    length[(a - 1, b - 1)] = c
    length[(b - 1, a - 1)] = c

r = 0
dist = [0] * N

prv = [None] * N
depth = [0] * N


def dfs(v):
    for u in G[v]:
        if dist[u] > 0 or u == r: continue
        dist[u] = dist[v] + length[(v, u)]
        depth[u] = depth[v] + 1
        prv[u] = v
        dfs(u)


dfs(r)

# N: 頂点数
# G[v]: 頂点vの子頂点 (親頂点は含まない)
#
# - construct
# prv[u] = v: 頂点uの一つ上の祖先頂点v
# - lca
# kprv[k][u] = v: 頂点uの2^k個上の祖先頂点v
# depth[u]: 頂点uの深さ (根頂点は0)

LV = (N - 1).bit_length()


def construct(prv):
    kprv = [prv]
    S = prv
    for k in range(LV):
        T = [0] * N
        for i in range(N):
            if S[i] is None:
                continue
            T[i] = S[S[i]]
        kprv.append(T)
        S = T
    return kprv


def lca(u, v, kprv, depth):
    dd = depth[v] - depth[u]
    if dd < 0:
        u, v = v, u
        dd = -dd

    # assert depth[u] <= depth[v]
    for k in range(LV + 1):
        if dd & 1:
            v = kprv[k][v]
        dd >>= 1

    # assert depth[u] == depth[v]
    if u == v:
        return u

    for k in range(LV - 1, -1, -1):
        pu = kprv[k][u]; pv = kprv[k][v]
        if pu != pv:
            u = pu; v = pv

    # assert kprv[0][u] == kprv[0][v]
    return kprv[0][u]


kprv = construct(prv)

Q, K = map(int, input().split())
K -= 1

ans = []
for _ in range(Q):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    xr = lca(x, K, kprv, depth)
    yr = lca(y, K, kprv, depth)
    a = dist[x] + dist[K] - dist[xr] * 2 + dist[y] + dist[K] - dist[yr] * 2
    ans.append(a)

print('\n'.join(map(str, ans)))
