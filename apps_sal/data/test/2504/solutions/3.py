import numpy as np
from scipy.sparse.csgraph import floyd_warshall

N, M, L = list(map(int, input().split()))
Map = np.full((N, N), 10**12, dtype='int64')
for _ in range(M):
    a, b, c = list(map(int, input().split()))
    a -= 1
    b -= 1
    Map[a][b] = c
    Map[b][a] = c
Q = int(input())
Query = [tuple(map(int, input().split())) for _ in range(Q)]
graph = floyd_warshall(Map).astype('int64')
graph[graph <= L] = 1
graph[graph > L] = 10**12
A = floyd_warshall(graph).astype('int64')
for s, t in Query:
    if A[s - 1][t - 1] >= 10**12:
        print((-1))
    else:
        print((int(A[s - 1][t - 1] - 1)))

