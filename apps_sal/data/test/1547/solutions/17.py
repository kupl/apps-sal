import sys
n, m, k = [int(x) for x in input().split()]
lines, columns = [(0, 0, i, 1) for i in range(n)], [(0, 0, i, 2) for i in range(m)]
for i, line in enumerate(sys.stdin):
    t, r, c = [int(x) for x in line.split()]
    if t == 1:
        lines[r - 1] = (i, c, r - 1, 1)
    else:
        columns[r - 1] = (i, c, r - 1, 2)
strings = lines + columns
strings.sort()
matrix = [[0] * m for i in range(n)]
for i, c, r, t in strings:
    if t == 1:
        matrix[r] = [c for i in range(m)]
    else:
        for j in range(n):
            matrix[j][r] = c

for i in range(n):
    sys.stdout.write(' '.join(map(str, matrix[i])) + '\n')
