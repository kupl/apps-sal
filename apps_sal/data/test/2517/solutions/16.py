import itertools
import numpy as np
from scipy.sparse.csgraph import shortest_path

N, M, R = map(int, input().split())
rs = np.array(list(map(int, input().split()))) - 1

nodes = np.full((N, N), np.inf)
for i in range(M):
    a, b, c = map(int, input().split())
    nodes[a - 1, b - 1] = nodes[b - 1, a - 1] = c
min_ds = shortest_path(nodes)
res = float('inf')
for p in itertools.permutations(rs):
    prev = p[0]
    tmp = 0
    for next in p[1:]:
        tmp += min_ds[prev, next]
        prev = next
    res = min(res, tmp)

print(int(res))
