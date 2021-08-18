from scipy.sparse.csgraph import floyd_warshall
import numpy as np


def warshall_floyd(graph):
    num_v = len(graph)

    for k in range(num_v):
        for i in range(num_v):
            for j in range(num_v):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
    return graph


N = int(input())
graph = [[float("inf") for _ in range(N)] for _ in range(N)]
for i in range(N):
    a_list = list(map(int, input().split()))
    for j in range(N):
        if i == j:
            continue
        graph[i][j] = a_list[j]
# import copy
# a_list = copy.deepcopy(graph)
w_graph = floyd_warshall(graph, directed=False)
result = 0
for i in range(N):
    w_graph[i][i] = float("inf")
for i in range(N):
    for j in range(i):
        if i == j:
            continue
        if w_graph[i][j] != graph[i][j]:
            print((-1))
            return
        if w_graph[i][j] < np.min(w_graph[i] + w_graph[j]):
            result += w_graph[i][j]
print((int(result)))
