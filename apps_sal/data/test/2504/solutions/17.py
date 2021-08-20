import sys
import numpy as np
from scipy.sparse.csgraph import floyd_warshall
from scipy.sparse import csr_matrix
input = sys.stdin.readline
cost = []
row = []
col = []
(n, m, l) = list(map(int, input().split()))
for _ in range(m):
    (a, b, c) = list(map(int, input().split()))
    cost.append(c)
    row.append(a - 1)
    col.append(b - 1)
q = int(input())
st = [list(map(int, input().split())) for _ in range(q)]
csr = csr_matrix((cost, (row, col)), shape=(n, n))
path = floyd_warshall(csr, directed=False)
cost = []
row = []
col = []
for i in range(n):
    for j in range(n):
        if path[i][j] <= l:
            cost.append(1)
            row.append(i)
            col.append(j)
csr = csr_matrix((cost, (row, col)), shape=(n, n))
path = floyd_warshall(csr, directed=False)
INF = float('inf')
for (s, t) in st:
    ans = path[s - 1][t - 1]
    if ans == INF:
        print(-1)
    else:
        print(int(ans) - 1)
