from scipy.sparse.csgraph import csgraph_from_dense, floyd_warshall
from itertools import permutations

N, M, R = list(map(int, input().split()))
r = list(map(int, input().split()))

d = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    A, B, C = list(map(int, input().split()))
    d[A][B] = C
    d[B][A] = C
g = csgraph_from_dense(d)
g = floyd_warshall(g)

result = 1000000000
for p in permutations(r):
    t = 0
    for i in range(R - 1):
        t += g[p[i]][p[i + 1]]
    result = min(result, t)
print((int(result)))
