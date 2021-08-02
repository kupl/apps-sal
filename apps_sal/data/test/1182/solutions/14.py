r, c, n, k = list(map(int, input().split()))
d = [[0 for j in range(c + 1)] for i in range(r + 1)]
for i in range(n):
    x, y = list(map(int, input().split()))
    d[x][y] = 1
for i in range(1, r + 1):
    for j in range(1, c + 1):
        d[i][j] = d[i][j] + d[i - 1][j] + d[i][j - 1] - d[i - 1][j - 1]
a = 0
for i in range(1, r + 1):
    for j in range(1, c + 1):
        for x in range(i, r + 1):
            for y in range(j, c + 1):
                if d[x][y] - d[x][j - 1] - d[i - 1][y] + d[i - 1][j - 1] >= k:
                    a += 1

print(a)
