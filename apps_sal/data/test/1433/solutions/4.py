from sys import stdin as fin

n, m = map(int, fin.readline().split())
mtrx = [list(map(int, fin.readline().split())) for i in range(n)]

lines, cols = [[0] * m for i in range(n)], [[0] * n for i in range(m)]

for i in range(n):
    for j in range(m):
        if mtrx[i][j] == 1:
            lines[i][j] = 1
            cols[j][i] = 1

for i in range(n):
    for j in range(1, m):
        lines[i][j] += lines[i][j - 1]

for j in range(m):
    for i in range(1, n):
        cols[j][i] += cols[j][i - 1]

cnt = 0
for i in range(n):
    for j in range(m):
        if mtrx[i][j] == 0:
            cnt += (1 if lines[i][j] else 0) + (1 if (lines[i][m - 1] - lines[i][j]) else 0) +\
                (1 if cols[j][i] else 0) + (1 if (cols[j][n - 1] - cols[j][i]) else 0)
print(cnt)
