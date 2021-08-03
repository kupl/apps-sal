from scipy.sparse.csgraph import dijkstra
import numpy as np
n = int(input())
a = [0] + [int(j)for j in input().split()]
graph = np.zeros((n + 2, n + 2), dtype=np.int64)
start, goal = 0, n + 1
for i, j in enumerate(a[1:], 1):
    if j >= 0:
        graph[start, i] = j
    else:
        graph[i, goal] = -j
for i in range(1, n + 1):
    for j in range(2 * i, n + 1, i):
        graph[j, i] = 10**18


def max_flow(graph):
    flow = 0
    while True:
        dist, pred = dijkstra(graph, indices=start, return_predecessors=True, unweighted=True)
        if dist[goal] == np.inf:
            return flow
        path = []
        v = goal
        while True:
            path.append((pred[v], v))
            v = pred[v]
            if v == start:
                break
        add_flow = min(graph[x][y] for x, y in path)
        for x, y in path:
            graph[x][y] -= add_flow
            graph[y][x] += add_flow
        flow += add_flow


print(sum(i for i in a if i > 0) - max_flow(graph))
