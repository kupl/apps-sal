import sys
from scipy.sparse.csgraph import floyd_warshall
(N, M, L) = list(map(int, input().split()))
INF = 10 ** 9 + 1
G = [[float('inf')] * N for i in range(N)]
for i in range(M):
    (a, b, c) = list(map(int, sys.stdin.readline().split()))
    (a, b) = (a - 1, b - 1)
    G[a][b] = c
    G[b][a] = c
G = floyd_warshall(G)
E = [[float('inf')] * N for i in range(N)]
for i in range(N):
    for j in range(N):
        if G[i][j] <= L:
            E[i][j] = 1
E = floyd_warshall(E)
Q = int(input())
for i in range(Q):
    (s, t) = list(map(int, sys.stdin.readline().split()))
    (s, t) = (s - 1, t - 1)
    print(int(E[s][t] - 1) if E[s][t] != float('inf') else -1)
