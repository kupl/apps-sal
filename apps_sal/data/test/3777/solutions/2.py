import sys
mod = 10 ** 9 + 7
sys.setrecursionlimit(mod)
input = sys.stdin.readline

def root(v):
    if v == par[v]:
        return v
    par[v] = root(par[v])
    return par[v]

def unite(u, v):
    u = root(u)
    v = root(v)
    if u == v:
        return
    if rank[u] < rank[v]:
        u, v = v, u
    par[v] = u
    if rank[u] == rank[v]:
        rank[u] += 1

def same(u, v):
    return root(u) == root(v)

def kruskal(edges):
    tree = [[] for _ in range(N)]
    used = [False] * M
    weight = 0
    for i, (w, u, v) in enumerate(edges):
        if same(u, v):
            continue
        unite(u, v)
        weight += w
        tree[u].append((w, v))
        tree[v].append((w, u))
        used[i] = True
    return weight, tree, used

def dfs(v=0, p=-1, d=0, w=0):
    parent[0][v] = p
    depth[v] = d
    max_w[0][v] = w
    for w, u in T[v]:
        if u == p:
            continue
        dfs(u, v, d+1, w)

def lca(u, v):
    if depth[u] > depth[v]:
        u, v = v, u
    tmp = 0
    while depth[v] > depth[u]:
        diff = depth[v] - depth[u]
        k = diff.bit_length() - 1
        tmp = max(tmp, max_w[k][v])
        v = parent[k][v]
    if u == v:
        return tmp
    for k in range(logN-1, -1, -1):
        if parent[k][u] != parent[k][v]:
            tmp = max(tmp, max_w[k][u], max_w[k][v])
            u = parent[k][u]
            v = parent[k][v]
    return max(tmp, max_w[0][u], max_w[0][v])

def modpow(x, p):
    if p == 0:
        return 1
    elif p == 1:
        return x % mod
    if p % 2 == 1:
        return x * modpow(x, p-1) % mod
    return modpow(x * x % mod, p // 2) % mod

N, M = map(int, input().split())
logN = (N - 1).bit_length()
X = int(input())
E = [tuple()] * M
for i in range(M):
    u, v, w = map(int, input().split())
    E[i] = (w, u-1, v-1)
E = sorted(E, key=lambda x: x[0])
par = list(range(N))
rank = [1] * N
W, T, F = kruskal(E)
depth = [0] * N
parent = [[0] * N for _ in range(logN+1)]
max_w = [[0] * N for _ in range(logN+1)]
dfs()
for k in range(logN):
    for v in range(N):
        if parent[k][v] < 0:
            parent[k+1][v] = -1
            max_w[k+1][v] = max_w[k][v]
        else:
            parent[k+1][v] = parent[k][parent[k][v]]
            max_w[k+1][v] = max(max_w[k][v], max_w[k][parent[k][v]])

le = 0
eq = 0
ge = 0
for i, (w, u, v) in enumerate(E):
    s = W
    if not F[i]:
        s += (w - lca(u, v))
    if s < X:
        le += 1
    else:
        if s == X:
            eq += 1
        else:
            ge += 1
ans = 0
if eq != 0:
    if le == 0:
        ans = (modpow(2, eq) - 2) * modpow(2, ge) % mod
    else:
        ans = 2 * (modpow(2, eq) - 1) * modpow(2, ge) % mod
print(ans)
