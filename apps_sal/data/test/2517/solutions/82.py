from itertools import permutations
from scipy.sparse.csgraph import floyd_warshall
import numpy as np
N, M, R = list(map(int, input().split()))
r = tuple(map(int, input().split()))

inf = 10**9
graph = np.ones((N, N), dtype=int)*inf
for _ in range(M):
    a, b, c = list(map(int, input().split()))
    a -= 1
    b -= 1
    graph[a][b] = c
    graph[b][a] = c
fy = floyd_warshall(graph)

ans = 10 ** 9
for p in permutations(r):
    tmp = 0
    for x, y in zip(p[:-1], p[1:]):
        x -= 1
        y -= 1
        tmp += int(fy[x][y])
    ans = min(ans, tmp)
print(ans)

