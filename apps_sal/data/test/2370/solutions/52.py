N = int(input())
graph = [[float("inf") for _ in range(N)] for _ in range(N)]
for i in range(N):
    a_list = list(map(int, input().split()))
    for j in range(N):
        if i == j:
            continue
        graph[i][j] = a_list[j]
import numpy as np
from scipy.sparse.csgraph import floyd_warshall
w_graph = floyd_warshall(graph, directed=False)
for i in range(N):
    w_graph[i][i] = float("inf")
result = 0
for i in range(N):
     w_graph[i][i] = float("inf")
for i in range(N):
    for j in range(i):
        if w_graph[i][j] != graph[i][j]:
            print((-1))
            return
        if w_graph[i][j] < np.min(w_graph[i] + w_graph[j]):
            result += w_graph[i][j]
print((int(result)))

