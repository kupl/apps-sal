import numpy as np
from scipy.sparse.csgraph import shortest_path, floyd_warshall, dijkstra, bellman_ford, johnson
from scipy.sparse import csr_matrix

h, w = map(int, input().split())

c = []
for i in range(10):
    c.append(list(map(int, input().split())))

csr = csr_matrix(c)

a = []
for i in range(h):
    a.append(list(map(int, input().split())))

cost = floyd_warshall(csr)[:, 1]

ans = 0
for i in range(h):
    for j in range(w):
        if a[i][j] > -1:
            ans += int(cost[a[i][j]])
print(ans)
