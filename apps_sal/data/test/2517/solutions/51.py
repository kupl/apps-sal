from itertools import permutations, combinations
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import dijkstra
N, M, R = map(int, input().split())
r = list(map(int, input().split()))
r = [r[i] - 1 for i in range(R)]
vve = [list(map(int, input().split())) for i in range(M)]
v1, v2, edge = zip(*vve)
v1 = list(v1)
v2 = list(v2)
for i in range(M):
    v1[i] -= 1
    v2[i] -= 1
csr = csr_matrix((edge, (v1, v2)), shape=(N, N))
dist = [[0 for j in range(R)] for i in range(R)]
for i, j in combinations(range(R), 2):
    r1, r2 = r[i], r[j]
    dist[i][j] = int(dijkstra(csr, directed=False, indices=r1)[r2])
    dist[j][i] = dist[i][j]
ans = 10**18
for x in permutations(range(R)):
    distsum = 0
    for i in range(1, R):
        distsum += dist[x[i]][x[i - 1]]
    ans = min(ans, distsum)
print(ans)
