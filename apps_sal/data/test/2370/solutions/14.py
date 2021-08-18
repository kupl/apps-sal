
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
    answer += d
    dist[x, y] = d
    dist[y, x] = d
    dist_use_xy = np.add.outer(dist[:, x], dist[:, y]) + d
    dist = np.minimum(dist, np.minimum(dist_use_xy, dist_use_xy.T))

print(answer)
