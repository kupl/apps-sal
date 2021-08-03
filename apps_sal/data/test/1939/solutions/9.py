from copy import deepcopy
n, k = map(int, input().split())


def fill_matrix(n):
    data = []
    q = [0] * n
    for i in range(n):
        data.append(deepcopy(q))
    return data


def E_matrix(matrix):
    for i in range(n):
        matrix[i][i] = k


matrix = fill_matrix(n)


E_matrix(matrix)


for row in matrix:
    sep = ' '
    for col in row:
        print(col, end=sep)
    print('')
