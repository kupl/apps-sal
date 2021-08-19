# !!!!!!
from sys import stdin as fin
# fin = open("t2b.in")

# n = int(fin.readline())
n, m = map(int, fin.readline().split())
# line = fin.readline().strip()
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
    # print(' '.join(str(n) for n in lines[i]))
# print()

for j in range(m):
    for i in range(1, n):
        cols[j][i] += cols[j][i - 1]
    # print(' '.join(str(n) for n in cols[j]))
# print()

cnt = 0
for i in range(n):
    for j in range(m):
        if mtrx[i][j] == 0:
            # print((i, j), lines[i][j], lines[i][m - 1] - lines[i][j], cols[j][i], cols[j][n - 1] - cols[j][i])
            cnt += (1 if lines[i][j] else 0) + (1 if (lines[i][m - 1] - lines[i][j]) else 0) +\
                (1 if cols[j][i] else 0) + (1 if (cols[j][n - 1] - cols[j][i]) else 0)
print(cnt)
