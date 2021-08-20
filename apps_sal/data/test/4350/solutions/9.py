(n, m) = map(int, input().split())
mat = []
for i in range(n):
    mat.append(list(map(int, input().replace('*', '1').replace('.', '0'))))
(ver, hor) = ([[0 for i in range(m)] for j in range(n)], [[0 for i in range(m)] for j in range(n)])
dp = [[[0 for i in range(4)] for j in range(m)] for k in range(n)]
for i in range(1, n):
    for j in range(1, m):
        (x, y) = (n - i - 1, m - j - 1)
        if mat[i][j] == 1:
            dp[i][j][0] = max(dp[i][j - 1][0], mat[i][j - 1]) + 1
            dp[i][j][1] = max(dp[i - 1][j][1], mat[i - 1][j]) + 1
        if mat[x][y] == 1:
            dp[x][y][2] = max(dp[x][y + 1][2], mat[x][y + 1]) + 1
            dp[x][y][3] = max(dp[x + 1][y][3], mat[x + 1][y]) + 1
stars = []
for i in range(1, n - 1):
    for j in range(1, m - 1):
        if mat[i][j] == 1:
            s = min(dp[i][j]) - 1
            if s > 0:
                stars.append((i + 1, j + 1, s))
                ver[i - s][j] += 1
                if i + s + 1 < n:
                    ver[i + s + 1][j] -= 1
                hor[i][j - s] += 1
                if j + s + 1 < m:
                    hor[i][j + s + 1] -= 1
for i in range(1, n):
    for j in range(1, m):
        ver[i][j] += ver[i - 1][j]
        hor[i][j] += hor[i][j - 1]
chk = True
for i in range(n):
    for j in range(m):
        if mat[i][j] and max(ver[i][j], hor[i][j]) <= 0:
            chk = False
            break
if chk:
    print(len(stars))
    for i in stars:
        print(*i)
else:
    print(-1)
