# 小さい距離から見ていく
# 既に作った道の範囲で、任意の2点の最短距離を持っておく
# 既存の最短距離より大きい：矛盾
# 既存の最短距離と等しい：増やしても何も変わらず
# 既存の最短距離より小さい：追加する必要あり

import numpy as np
N = int(input())
A = [[int(x) for x in input().split()] for _ in range(N)]

edge = []

for i in range(N):
    for j in range(i):
        edge.append((A[i][j], j, i))
edge.sort()

INF = 10**18
dist = np.full((N, N), INF, dtype=np.int64) - np.eye(N, dtype=np.int64) * INF

answer = 0
for d, x, y in edge:
    if d > dist[x, y]:
        answer = -1
        break
    if d == dist[x, y]:
        continue
    # 追加
    answer += d
    dist[x, y] = d
    dist[y, x] = d
    # 距離行列の更新
    # (i,j) -> (i,x),(x,y),(y,j)
    dist_use_xy = np.add.outer(dist[:, x], dist[:, y]) + d
    dist = np.minimum(dist, np.minimum(dist_use_xy, dist_use_xy.T))

print(answer)
