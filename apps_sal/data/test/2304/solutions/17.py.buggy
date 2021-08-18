from collections import defaultdict, deque
import sys
readline = sys.stdin.readline
sys.setrecursionlimit(10**8)
mod = 10**9 + 7
#mod = 998244353
INF = 10**9
eps = 10**-7

N, M = list(map(int, input().split()))
# 1-indexed union-find
# parent(親)
par = [i for i in range(N + 1)]
# rank(深さ)
rank = [0] * (N + 1)
# 同グループの頂点数
# size = [1]*(N+1)

# 木の根を求める


def root(x):
    if par[x] == x:             # 根の時
        return x
    else:
        par[x] = root(par[x])   # 経路圧縮
        return par[x]

# xとyの属する集合を併合(ランク有)


def unite(x, y):
    x = root(x)
    y = root(y)
    if x == y:
        return
    if rank[x] < rank[y]:
        par[x] = y              # xの親をyに
        # size[y] += size[x]      # yの頂点数+=xの頂点数
    else:
        par[y] = x              # yの親をxに
        # size[x] += size[y]      # xの頂点数+=yの頂点数
        if rank[x] == rank[y]:
            rank[x] += 1


LRD = [tuple(map(int, readline().split())) for i in range(M)]

for (L, R, D) in LRD:
    unite(L, R)

rel = defaultdict(lambda: [])

for (L, R, D) in LRD:
    rel[root(L)].append((L, R, D))

for k, v in list(rel.items()):
    dist = defaultdict(lambda: [])
    for (L, R, D) in v:
        dist[L].append((R, D))
        dist[R].append((L, -D))
    que = deque([])
    x = {}
    for k1, v1 in list(dist.items()):
        x[k1] = 0
        for (to, dis) in v1:
            x[to] = dis
            que.append(to)
        break
    while que:
        fro = que.popleft()
        for (to, dis) in dist[fro]:
            if to not in list(x.keys()):
                x[to] = x[fro] + dis
                que.append(to)
    for (L, R, D) in v:
        if x[R] - x[L] != D:
            print('No')
            return
print('Yes')
