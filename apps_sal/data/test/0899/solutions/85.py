import numpy as np
from scipy.sparse.csgraph import floyd_warshall
from scipy.sparse import csr_matrix

n, w = map(int, input().split())

edges = []

d = [[float("inf")] * n for _ in range(n)]
for i in range(w):
    x, y, z = map(int, input().split())
    x -= 1
    y -= 1
    d[x][y] = z
    d[y][x] = z
    edges.append((x, y, z))

for i in range(n):
    d[i][i] = 0
# print("d",d)

csr = csr_matrix(d)
dp = floyd_warshall(csr)
ans = 0
# print("dp",dp)

for i, j, c in edges:
    # print(i,j,c)
    if dp[i, j] < c:
        ans += 1
print(ans)
