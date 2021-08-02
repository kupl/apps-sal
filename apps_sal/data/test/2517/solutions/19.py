import itertools
from scipy.sparse.csgraph import csgraph_from_dense, floyd_warshall
N, M, R = list(map(int, input().split()))
r = [int(i) for i in input().split()]

G = [[10**8] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    A, B, C = list(map(int, input().split()))
    G[A][B] = C
    G[B][A] = C

DG = csgraph_from_dense(G, null_value=10**8)
d = floyd_warshall(DG)

ans = 10**8
for route in itertools.permutations(r):
    c = 0
    for i in range(len(route) - 1):
        c += d[route[i]][route[i + 1]]
    ans = min(ans, c)
print((int(ans)))
