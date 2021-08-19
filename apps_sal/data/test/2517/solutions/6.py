import itertools
from scipy.sparse.csgraph import floyd_warshall
(N, M, R) = list(map(int, input().split()))
r = tuple(map(int, input().split()))
INF = 10 ** 10
d = [[INF] * N for _ in range(N)]
for i in range(N):
    d[i][i] = 0
for _ in range(M):
    (a, b, c) = list(map(int, input().split()))
    a -= 1
    b -= 1
    if d[a][b] > c:
        d[a][b] = c
        d[b][a] = c
d = floyd_warshall(d)
ans = INF
for p in itertools.permutations(r):
    dist = 0
    for i in range(R - 1):
        dist += d[p[i] - 1][p[i + 1] - 1]
    ans = min(ans, dist)
print(int(ans))
