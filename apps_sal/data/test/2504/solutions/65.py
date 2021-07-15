import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import floyd_warshall

n, m, l = map(int, input().split())
INF = 1 << 60

# 距離のmatrixを作る
dist = [[INF] * n for _ in range(n)]

# 対角行列の成分は０
for i in range(n):
    dist[i][i] = 0

# 燃料の最大値より小さい場合に辺が張れる
for _ in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    if c > l:
        continue
    dist[a][b] = c
    dist[b][a] = c

# 全点間の最短距離を求める
dist = floyd_warshall(csr_matrix(dist))

# 初期状態を１にする。燃料が足りない経路は迂回したいのでINFを置いておく
dist2 = np.full_like(dist, 1)
dist2[np.where(dist > l)] = INF

# 足し込むことで何回給油するべきかがわかる
dist2 = floyd_warshall(dist2, directed=False)
dist2 = dist2.astype(int)

# 無限大の経路は辿れない。-1を出力したいので０を置いていく
dist2[dist2 == INF] = 0

q = int(input())

# 初期状態を１としているので、１を引いて答えとする
ans = []
for _ in range(q):
    s, t = map(int, input().split())
    ans.append(dist2[s - 1, t - 1] - 1)

print(*ans, sep="\n")
