from itertools import permutations
from scipy.sparse.csgraph import csgraph_from_dense, floyd_warshall
inf = 10 ** 10
n, m, r = map(int, input().split())
R = list(map(int, input().split()))

edge = [[inf] * n for i in range(n)]
for i in range(m):
    a, b, c = map(int, input().split())
    edge[a - 1][b - 1] = c

G = csgraph_from_dense(edge, null_value=inf)
d = floyd_warshall(G, False)

rec = inf
for i in permutations(R, r):
    temp = 0
    for j in range(r):
        if j == r - 1:
            continue
        temp += d[i[j] - 1][i[j + 1] - 1]
    rec = min(rec, temp)

print(int(rec))
