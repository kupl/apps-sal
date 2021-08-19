import sys
import numpy as np
from scipy.sparse.csgraph import shortest_path
from scipy.sparse import csr_matrix
input = sys.stdin.readline
(n, m, l) = list(map(int, input().split()))
g_dense = np.zeros((n, n))
for _ in range(m):
    (a, b, c) = map(int, input().split())
    g_dense[a - 1][b - 1] = c
q = int(input())
st = [list(map(int, input().split())) for _ in range(q)]
path = shortest_path(g_dense, directed=False)
g_dense = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        if path[i][j] <= l:
            g_dense[i][j] = 1
path = shortest_path(g_dense, directed=False)
INF = float('inf')
for (s, t) in st:
    ans = path[s - 1][t - 1]
    if ans == INF:
        print(-1)
    else:
        print(int(ans) - 1)
