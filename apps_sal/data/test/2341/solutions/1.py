import sys
input = sys.stdin.readline
(n, m) = list(map(int, input().split()))
MAP = [input().strip() for i in range(n)]
COUNT0 = [[1] * m for i in range(n)]
COUNT1 = [[1] * m for i in range(n)]
COUNT2 = [[1] * m for i in range(n)]
COUNT3 = [[1] * m for i in range(n)]
for i in range(1, n - 1):
    for j in range(1, m - 1):
        if MAP[i][j] == MAP[i - 1][j] == MAP[i][j - 1]:
            COUNT0[i][j] = min(COUNT0[i - 1][j], COUNT0[i][j - 1]) + 1
for i in range(n - 2, 0, -1):
    for j in range(m - 2, 0, -1):
        if MAP[i][j] == MAP[i + 1][j] == MAP[i][j + 1]:
            COUNT1[i][j] = min(COUNT1[i + 1][j], COUNT1[i][j + 1]) + 1
for i in range(1, n - 1):
    for j in range(m - 2, 0, -1):
        if MAP[i][j] == MAP[i - 1][j] == MAP[i][j + 1]:
            COUNT2[i][j] = min(COUNT2[i - 1][j], COUNT2[i][j + 1]) + 1
for i in range(n - 2, 0, -1):
    for j in range(1, m - 1):
        if MAP[i][j] == MAP[i + 1][j] == MAP[i][j - 1]:
            COUNT3[i][j] = min(COUNT3[i + 1][j], COUNT3[i][j - 1]) + 1
ANS = 0
for i in range(n):
    for j in range(m):
        ANS += min(COUNT0[i][j], COUNT1[i][j], COUNT2[i][j], COUNT3[i][j])
print(ANS)
