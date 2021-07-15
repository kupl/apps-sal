from itertools import permutations
import numpy as np
from scipy.sparse.csgraph import dijkstra

with open(0) as f:
    N, M, R = map(int, f.readline().split())
    r = list(map(int, f.readline().split()))
    path = [tuple(map(int, line.split())) for line in f.readlines()]

graph = np.full((N,N), np.inf)
for a, b, c in path:
    graph[a-1, b-1] = c
    graph[b-1, a-1] = c

graph = dijkstra(graph, directed=False)
ans = np.inf
permutation = list(permutations(r))
for p in permutation:
    way = 0
    for x,y in zip(p[:len(r)], p[1:]):
        way += graph[x-1, y-1]
    ans = min(ans, way)
print(int(ans))
