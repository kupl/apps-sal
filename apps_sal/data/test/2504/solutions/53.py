import sys
import numpy as np
from scipy.sparse import*
F = csgraph.floyd_warshall
CSR = csr_matrix
input = sys.stdin.readline

n, m, l = map(int, input().split())
cost = [[0] * n for i in range(n)]
for i in range(m):
    a, b, c = map(int, input().split())
    cost[a - 1][b - 1] = c
    cost[b - 1][a - 1] = c

Cost = F(CSR(cost))
Cost = F(CSR(np.where((0 < Cost) & (Cost <= l), 1, 0)))

q = int(input())
for i in range(q):
    s, t = map(int, input().split())
    print(-1 if np.isinf(Cost[s - 1][t - 1]) else int(Cost[s - 1][t - 1]) - 1)
