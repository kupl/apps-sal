import numpy as np
from scipy.sparse.csgraph import floyd_warshall

N, M, L = list(map(int, input().split()))
INF = 1 << 31
dist = np.array([[INF for _ in range(N)] for _ in range(N)])

for i in range(N):
    dist[i][i] = 0

for i in range(M):
    a, b, c = list(map(int, input().split()))
    a -= 1
    b -= 1
    dist[a][b] = c
    dist[b][a] = c

dist = floyd_warshall(dist)

for i in range(N):
    for j in range(N):
        if dist[i][j] <= L:
            dist[i][j] = 1
        else:
            dist[i][j] = INF

dist = floyd_warshall(dist)
dist[dist == INF] = 0
# dist=dist.astype(int)
# print(dist)

Q = int(input())
ans = [0] * Q
for q in range(Q):
    s, t = list(map(int, input().split()))
    s -= 1
    t -= 1
    ans[q] = int(dist[s][t] - 1)

for a in ans:
    print((-1 if a == INF else a))
