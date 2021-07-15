import sys
input = sys.stdin.readline

import numpy as np
from scipy.sparse.csgraph import shortest_path, floyd_warshall, dijkstra, bellman_ford, johnson
from scipy.sparse import csr_matrix

H,W = map(int,input().split())
costs = []
for i in range(10):
    cost = list(map(int,input().split()))
    costs.append(cost)

cost_array = np.array(costs)
counter = [0]*10
for i in range(H):
    wall = list(map(int,input().split()))
    for j in wall:
        if j != -1:
            counter[j] += 1
mincost = shortest_path(cost_array)
ans = 0
for i in range(10):
    ans += counter[i] * mincost[i][1]
print(int(ans))
