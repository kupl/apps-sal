import itertools
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import shortest_path, floyd_warshall, dijkstra, bellman_ford, johnson
import numpy as np
n, m, r = list(map(int, input().split()))
r_list = list(map(int, input().split()))
matrix = [[float("inf") for i in range(n)] for j in range(n)]
for c in range(n):
    matrix[c][c] = 0
for v in range(m):
    a, b, c = list(map(int, input().split()))
    if matrix[a - 1][b - 1] > c:
        matrix[a - 1][b - 1] = c
        matrix[b - 1][a - 1] = c
matrix = np.array(matrix)
load = shortest_path(matrix, directed=False)
ans_list = []
for balls in itertools.permutations(r_list):
    balls = list(balls)
    ans = 0
    for i in range(1, len(r_list)):
        ans += load[balls[i - 1] - 1][balls[i] - 1]
    ans_list.append(int(ans))

print((min(ans_list)))
