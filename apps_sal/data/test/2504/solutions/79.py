import sys
input = sys.stdin.readline

N, M, L = (int(i) for i in input().split())

import numpy as np
from scipy.sparse.csgraph import floyd_warshall
from scipy.sparse import csr_matrix

graph = [[0]*N for i in range(N)]
for i in range(M):
    a, b, c = (int(i) for i in input().split())
    graph[a-1][b-1] = c
    graph[b-1][a-1] = c

graph = csr_matrix(graph)
d = floyd_warshall(csgraph=graph, directed=False)

new_graph = [[0]*N for i in range(N)]
for i in range(N):
    for j in range(N):
        if d[i][j] <= L:
            new_graph[i][j] = 1
            new_graph[j][i] = 1

graph = csr_matrix(new_graph)
d = floyd_warshall(csgraph=graph, directed=False)
Q = int(input())
for i in range(Q):
    s, t = (int(i) for i in input().split())
    if d[s-1][t-1] == float("inf"):
        print("-1")
    else:
        print(int(d[s-1][t-1]-1))
