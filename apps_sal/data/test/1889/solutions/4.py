(n, m, q) = [int(c) for c in input().split()]
matrix = []
for i in range(n):
    matrix.append([int(c) for c in input().split()])
maxperrow = []
for a in range(n):
    maxrow = 0
    maxmax = 0
    for b in range(m):
        if matrix[a][b] == 1:
            maxrow += 1
            if maxrow > maxmax:
                maxmax = maxrow
        else:
            maxrow = 0
    maxperrow.append(maxmax)
winner = []
for step in range(q):
    (i, j) = [int(c) for c in input().split()]
    matrix[i - 1][j - 1] = 1 - matrix[i - 1][j - 1]
    maxmax = 0
    maxrow = 0
    for b in range(m):
        if matrix[i - 1][b] == 1:
            maxrow += 1
            if maxrow > maxmax:
                maxmax = maxrow
        else:
            maxrow = 0
    maxperrow[i - 1] = maxmax
    winner.append(max(maxperrow))
for w in winner:
    print(w)
