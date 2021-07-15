from scipy.sparse.csgraph import floyd_warshall
import numpy as np

N, M, L = list(map(int, input().split()))
inf = 10**9 + 1
dist = [[inf] * N for i in range(N)]
for i in range(M):
    A, B, C = list(map(int, input().split()))
    dist[A-1][B-1] = dist[B-1][A-1] = C

dist = floyd_warshall(dist, directed=False)
dist = np.where(dist <= L, 1, inf)
dist = floyd_warshall(dist, directed=False)
dist = np.where(dist < inf, dist-1, -1)

Q = int(input())
for i in range(Q):
    s, t = list(map(int, input().split()))
    print((int(dist[s-1, t-1])))

