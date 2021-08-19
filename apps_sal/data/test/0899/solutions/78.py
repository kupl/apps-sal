(N, M) = map(int, input().split())


def warshall_floyd(d):
    for k in range(N):
        for i in range(N):
            for j in range(N):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return d


d = [[float('inf')] * N for i in range(N)]
A = []
for i in range(M):
    (x, y, z) = map(int, input().split())
    x -= 1
    y -= 1
    d[x][y] = z
    d[y][x] = z
    A.append((x, y, z))
for i in range(N):
    d[i][i] = 0
D = warshall_floyd(d)
ans = 0
for (x, y, z) in A:
    if D[x][y] != z:
        ans += 1
print(ans)
