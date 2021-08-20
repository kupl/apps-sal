import numpy as np
import sys
from scipy.sparse.csgraph import floyd_warshall, csgraph_from_dense
from scipy.sparse import csr_matrix
input = sys.stdin.readline


def inputs():
    return [int(x) for x in input().split()]


(N, M, L) = inputs()
ABC = [inputs() for _ in range(M)]
graph = [[10 ** 13] * (N + 1) for _ in range(N + 1)]
for (a, b, c) in ABC:
    graph[a][b] = c
G = csgraph_from_dense(graph, null_value=10 ** 13)
dist_mat = floyd_warshall(graph, directed=False)
graph2 = np.array([[10 ** 13] * (N + 1) for _ in range(N + 1)])
np.fill_diagonal(graph2, 0)
graph2[dist_mat <= L] = 1
dist_mat2 = floyd_warshall(graph2, directed=False)
dist_mat2[dist_mat2 == 10 ** 13] = 0
Q = int(input())
for i in range(Q):
    (s, t) = inputs()
    print(int(dist_mat2[s, t]) - 1)
