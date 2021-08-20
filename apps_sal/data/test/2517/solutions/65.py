import itertools
import numpy as np
from scipy.sparse.csgraph import shortest_path, floyd_warshall, dijkstra, bellman_ford, johnson
(N, M, R) = map(int, input().split())
r_list = np.array(list(map(int, input().split()))) - 1
nodes = np.full((N, N), np.inf)
for i in range(M):
    (a, b, c) = map(int, input().split())
    nodes[a - 1, b - 1] = nodes[b - 1, a - 1] = c
min_ds = shortest_path(nodes)
res = 10 ** 9
for cmb in itertools.permutations(r_list):
    prev = cmb[0]
    tmpres = 0
    for to in cmb[1:]:
        tmpres += min_ds[prev, to]
        prev = to
    res = min(res, tmpres)
print(int(res))
