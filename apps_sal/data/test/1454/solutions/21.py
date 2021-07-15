def rising(matr, n, m):
    s = matr[n - 1][m - 1]
    for j in range(m - 2, -1, -1):
        if matr[n - 1][j] < matr[n - 1][j + 1]:
            if matr[n - 1][j] == 0:
                matr[n - 1][j] = matr[n - 1][j + 1] - 1
            s += matr[n - 1][j]
        else:
            return -1
    for i in range(n - 2, -1, -1):
        if matr[i][m - 1] < matr[i + 1][m - 1]:
            if matr[i][m - 1] == 0:
                matr[i][m - 1] = matr[i + 1][m - 1] - 1
            s += matr[i][m - 1]
        else:
            return -1
    for i in range(n - 2, -1, -1):
        for j in range(m - 2, -1, -1):
            if matr[i][j] < min(matr[i + 1][j], matr[i][j + 1]):
                if matr[i][j] == 0:
                    matr[i][j] = min(matr[i + 1][j], matr[i][j + 1]) - 1
                s += matr[i][j]
            else:
                return -1
    return s


N, M = [int(x) for x in input().split()]
matrix = list()
for y in range(N):
    row = [int(y) for y in input().split()]
    matrix.append(row)
print(rising(matrix, N, M))

