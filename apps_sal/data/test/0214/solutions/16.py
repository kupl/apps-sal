def go():
    matrix = []
    matrix.append(list(i for i in input()))
    matrix.append(list(i for i in input()))
    c = 0
    for i in range(len(matrix[0]) - 1):
        if matrix[0][i] == '0' and matrix[1][i] == '0':
            if matrix[0][i + 1] == '0':
                matrix[0][i] = 'X'
                matrix[1][i] = 'X'
                matrix[0][i + 1] = 'X'
                c += 1
            elif matrix[1][i + 1] == '0':
                matrix[0][i] = 'X'
                matrix[1][i] = 'X'
                matrix[1][i + 1] = 'X'
                c += 1
        elif matrix[0][i] == '0':
            if matrix[0][i + 1] == '0' and matrix[1][i + 1] == '0':
                matrix[0][i] = 'X'
                matrix[0][i + 1] = 'X'
                matrix[1][i + 1] = 'X'
                c += 1
        elif matrix[1][i] == '0':
            if matrix[0][i + 1] == '0' and matrix[1][i + 1] == '0':
                matrix[1][i] = 'X'
                matrix[0][i + 1] = 'X'
                matrix[1][i + 1] = 'X'
                c += 1
    return c


print(go())
