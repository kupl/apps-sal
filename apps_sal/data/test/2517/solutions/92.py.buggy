N, M, K = (int(x) for x in input().split())
R = [int(x) - 1 for x in input().split()]

dist = [[10e8 for _ in range(N)] for _ in range(N)]
for i in range(N):
    dist[i][i] = 0
for _ in range(M):
    a, b, c = (int(x) for x in input().split())
    dist[a - 1][b - 1] = dist[b - 1][a - 1] = c
del a, b, c, K

for k in range(N):
    for i in range(N):
        for j in range(i, N):
            dist[i][j] = dist[j][i] = min(dist[i][j], dist[i][k] + dist[k][j])


def mindist(x, X):
    nonlocal dist
    Y = X.copy()
    Y.remove(x)
    if len(Y) == 0:
        return 0
    return min([dist[x][y] + mindist(y, Y) for y in Y])


ans = min([mindist(r, R) for r in R])
print(ans)
