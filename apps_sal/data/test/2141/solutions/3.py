n = int(input())
mat = [[0 for i in range(n)] for j in range(n)]
for i in range(n):
    for j in range(n):
        if (i + j) % 2 == 1:
            mat[i][j] = 'W'
        else:
            mat[i][j] = 'B'
for i in range(n):
    for j in range(n):
        if j < n - 1:
            print(mat[i][j], end='')
        else:
            print(mat[i][j])
