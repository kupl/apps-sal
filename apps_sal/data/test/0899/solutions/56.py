def warshall_floyd(d):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][k] + d[k][j], d[i][j])
    return d


(n, m) = list(map(int, input().split()))
d = [[float('INF')] * n for i in range(n)]
hen = [0] * m
for i in range(m):
    (x, y, z) = list(map(int, input().split()))
    d[x - 1][y - 1] = z
    d[y - 1][x - 1] = z
    hen[i] = [x - 1, y - 1, z]
for i in range(n):
    d[i][i] = 0
ans = warshall_floyd(d)
answer = 0
for i in range(m):
    now = hen[i]
    if d[now[0]][now[1]] != now[2]:
        answer += 1
print(answer)
