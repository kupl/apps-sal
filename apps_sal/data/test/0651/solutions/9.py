import sys
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
(rows, cols) = map(int, sys.stdin.readline().split())
b = ['' for row in range(rows)]
(sr, sc) = (0, 0)
(er, ec) = (0, 0)
for row in range(rows):
    b[row] = sys.stdin.readline().strip()
    if 'S' in b[row]:
        (sr, sc) = (row, b[row].index('S'))
    if 'E' in b[row]:
        (er, ec) = (row, b[row].index('E'))
dirs = sys.stdin.readline().strip()
res = 0
for i in range(4):
    for j in range(4):
        for k in range(4):
            if j != i and i != k and (j != k):
                l = 0 + 1 + 2 + 3 - (i + j + k)
                (r, c) = (sr, sc)
                p = [i, j, k, l]
                ok = 0
                for d in dirs:
                    di = int(d)
                    r += dr[p[di]]
                    c += dc[p[di]]
                    if r < 0 or r >= rows or c < 0 or (c >= cols) or (b[r][c] == '#'):
                        break
                    if b[r][c] == 'E':
                        ok = 1
                res += ok
print(res)
