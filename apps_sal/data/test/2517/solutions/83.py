from itertools import permutations
from scipy.sparse.csgraph import floyd_warshall
n, m, r = map(int, input().split())
R = list(map(int, input().split()))
l = [[float('inf')] * n for _ in range(n)]
for _ in range(m):
    a, b, c, = map(int, input().split())
    a -= 1
    b -= 1
    l[a][b] = c
    l[b][a] = c
for i in range(n):
    l[i][i] = 0


def warshall_floyd(d):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])

    return d


F1 = floyd_warshall(l)
ans = float('inf')
for v in permutations(R):
    temp = 0
    for i in range(r - 1):
        temp += F1[v[i] - 1][v[i + 1] - 1]
    ans = min(ans, temp)
print(int(ans))
