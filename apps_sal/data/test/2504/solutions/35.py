# import numpy as np
from scipy.sparse.csgraph import floyd_warshall
N, M, L = map(int, input().split())

INF = 10 ** 18
dist1 = [[INF] * N for _ in range(N)]
for i in range(N):
    dist1[i][i] = 0

for _ in range(M):
    A, B, C = map(int, input().split())
    A -= 1
    B -= 1
    dist1[A][B] = C
    dist1[B][A] = C

dist1 = floyd_warshall(dist1)

dist2 = [[INF] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if dist1[i][j] <= L:
            dist2[i][j] = 1

dist2 = floyd_warshall(dist2)

Q = int(input())
for _ in range(Q):
    s, t = map(int, input().split())
    s -= 1
    t -= 1
    if dist2[s][t] >= INF:
        print (-1)
    else:
        print (int(dist2[s][t] - 1))
