import numpy as np
from scipy.sparse.csgraph import shortest_path, floyd_warshall, dijkstra, bellman_ford, johnson
from scipy.sparse import csr_matrix
(N, M, L) = map(int, input().split())
d = [[0 for i in range(0, N)] for i in range(0, N)]
for i in range(0, M):
    (a, b, c) = map(int, input().split())
    d[a - 1][b - 1] = c
    d[b - 1][a - 1] = c
csr1 = csr_matrix(d)
a = floyd_warshall(csr1)
d = [[0 for i in range(0, N)] for j in range(0, N)]
for i in range(0, N):
    for j in range(0, N):
        if L >= a[i][j]:
            d[i][j] = 1
csr2 = csr_matrix(d)
data = floyd_warshall(csr2)
ans = []
Q = int(input())
for i in range(0, Q):
    (s, t) = map(int, input().split())
    if data[s - 1][t - 1] != float('inf'):
        ans.append(int(data[s - 1][t - 1]) - 1)
    else:
        ans.append(-1)
for i in range(Q):
    print(ans[i])
