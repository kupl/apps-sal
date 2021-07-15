from itertools import permutations
import numpy as np
from scipy.sparse.csgraph import dijkstra
from scipy.sparse import csr_matrix

N, M, R = map(int, input().split())
R = list(map(int, input().split()))
A, B, C = np.array([input().split() for _ in range(M)], dtype=int).T
G = csr_matrix((C, (A - 1, B - 1)), shape=(N, N))
path = dijkstra(G, directed=False)
path = (path + 0.5).astype(int)

ans = 10 ** 18
for p in permutations(R):
    cnt = 0
    for x, y in zip(p[:-1], p[1:]):
        x -= 1
        y -= 1
        cnt += path[x][y]
    ans = min(ans, cnt)

print(ans)
