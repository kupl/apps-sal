import itertools
import sys
from scipy.sparse.csgraph import csgraph_from_dense
from scipy.sparse.csgraph import dijkstra
input = sys.stdin.readline
(n, m, r) = list(map(int, input().split()))
visiting_town = list(map(int, input().split()))
edges = [[float('INF')] * n for _ in range(n)]
for i in range(m):
    (a, b, c) = list(map(int, input().split()))
    edges[a - 1][b - 1] = c
G = csgraph_from_dense(edges, null_value=float('INF'))
comp_dist = dijkstra(G, directed=False)
candidates = []
for route in itertools.permutations(visiting_town):
    result = 0
    for (_from, to) in zip(route[:-1], route[1:]):
        dist = comp_dist[_from - 1][to - 1]
        result += dist
    candidates.append(result)
print(int(min(candidates)))
