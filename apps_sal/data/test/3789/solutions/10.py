import numpy as np
from scipy.sparse.csgraph import dijkstra
import sys
input = sys.stdin.readline
'\n最小カット\n'
N = int(input())
start = 0
goal = N + 1
A = [0] + [int(x) for x in input().split()]
INF = 10 ** 12
graph = np.zeros((N + 2, N + 2), dtype=np.int64)
for (i, a) in enumerate(A[1:], 1):
    if a >= 0:
        graph[start, i] = a
    else:
        graph[i, goal] = -a
for i in range(1, N + 1):
    for j in range(2 * i, N + 1, i):
        if A[i] < 0 and A[j] > 0:
            graph[j][i] = INF


def max_flow(graph):
    flow = 0
    while True:
        (dist, pred) = dijkstra(graph, indices=start, return_predecessors=True, unweighted=True)
        if dist[goal] == np.inf:
            return flow
        path = []
        v = goal
        while True:
            path.append((pred[v], v))
            v = pred[v]
            if v == start:
                break
        add_flow = min((graph[x][y] for (x, y) in path))
        for (x, y) in path:
            graph[x][y] -= add_flow
            graph[y][x] += add_flow
        flow += add_flow


answer = sum((x for x in A if x > 0)) - max_flow(graph)
print(answer)
