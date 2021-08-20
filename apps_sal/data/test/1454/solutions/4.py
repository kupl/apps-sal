(n, m) = list(map(int, input().split(' ')))
matrix = []
for i in range(n):
    row = [int(x) for x in input().split(' ')]
    matrix.append(row)


def determine(matrix, n, m):
    sum_max = matrix[n - 1][m - 1]
    for j in range(m - 2, -1, -1):
        if matrix[n - 1][j] < matrix[n - 1][j + 1]:
            if matrix[n - 1][j] == 0:
                matrix[n - 1][j] = matrix[n - 1][j + 1] - 1
            sum_max += matrix[n - 1][j]
        else:
            return -1
    for i in range(n - 2, -1, -1):
        if matrix[i][m - 1] < matrix[i + 1][m - 1]:
            if matrix[i][m - 1] == 0:
                matrix[i][m - 1] = matrix[i + 1][m - 1] - 1
            sum_max += matrix[i][m - 1]
        else:
            return -1
    for i in range(n - 2, -1, -1):
        for j in range(m - 2, -1, -1):
            if matrix[i][j] < min(matrix[i + 1][j], matrix[i][j + 1]):
                if matrix[i][j] == 0:
                    matrix[i][j] = min(matrix[i + 1][j], matrix[i][j + 1]) - 1
                sum_max += matrix[i][j]
            else:
                return -1
    return sum_max


sum_max = determine(matrix, n, m)
print(sum_max)
