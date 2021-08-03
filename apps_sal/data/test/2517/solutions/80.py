import itertools
from scipy.sparse.csgraph import floyd_warshall

N, M, R = map(int, input().split())
r = tuple(map(int, input().split()))

INF = 10**10

d = [[INF] * N for _ in range(N)]

for i in range(N):
    d[i][i] = 0

for _ in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    if d[a][b] > c:
        d[a][b] = c
        d[b][a] = c


def warshall(d):
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if d[i][j] > d[i][k] + d[k][j]:
                    d[i][j] = d[i][k] + d[k][j]


# d = floyd_warshall(d)
warshall(d)


ans = INF
for p in itertools.permutations(r):
    dist = 0
    for i in range(R - 1):
        dist += d[p[i] - 1][p[i + 1] - 1]

    if ans > dist:
        ans = dist

print(int(ans))
