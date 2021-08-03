def is_win(matrix):
    variants = ['.XXXX', 'X.XXX', 'XX.XX', 'XXX.X', 'XXXX.']
    for i in matrix:
        for exp in variants:
            if exp in ''.join(i):
                return True
    new_matrix = []
    for i in range(10):
        matrix_part = []
        for j in matrix:
            matrix_part.append(j[i])
        new_matrix.append(matrix_part)
    for i in new_matrix:
        for exp in variants:
            if exp in ''.join(i):
                return True
    lines = [
        [matrix[0][0], matrix[1][1], matrix[2][2], matrix[3][3], matrix[4][4], matrix[5][5], matrix[6][6], matrix[7][7], matrix[8][8], matrix[9][9]],
        [matrix[0][1], matrix[1][2], matrix[2][3], matrix[3][4], matrix[4][5], matrix[5][6], matrix[6][7], matrix[7][8], matrix[8][9]],
        [matrix[0][2], matrix[1][3], matrix[2][4], matrix[3][5], matrix[4][6], matrix[5][7], matrix[6][8], matrix[7][9]],
        [matrix[0][3], matrix[1][4], matrix[2][5], matrix[3][6], matrix[4][7], matrix[5][8], matrix[6][9]],
        [matrix[0][4], matrix[1][5], matrix[2][6], matrix[3][7], matrix[4][8], matrix[5][9]],
        [matrix[0][5], matrix[1][6], matrix[2][7], matrix[3][8], matrix[4][9]],
        [matrix[1][0], matrix[2][1], matrix[3][2], matrix[4][3], matrix[5][4], matrix[6][5], matrix[7][6], matrix[8][7], matrix[9][8]],
        [matrix[2][0], matrix[3][1], matrix[4][2], matrix[5][3], matrix[6][4], matrix[7][5], matrix[8][6], matrix[9][7]],
        [matrix[3][0], matrix[4][1], matrix[5][2], matrix[6][3], matrix[7][4], matrix[8][5], matrix[9][6]],
        [matrix[4][0], matrix[5][1], matrix[6][2], matrix[7][3], matrix[8][4], matrix[9][5]],
        [matrix[5][0], matrix[6][1], matrix[7][2], matrix[8][3], matrix[9][4]],
    ]
    for line in lines:
        for exp in variants:
            if exp in ''.join(line):
                return True
    for i in range(10):
        matrix[i] = matrix[i][::-1]
    lines = [
        [matrix[0][0], matrix[1][1], matrix[2][2], matrix[3][3], matrix[4][4], matrix[5][5], matrix[6][6], matrix[7][7], matrix[8][8], matrix[9][9]],
        [matrix[0][1], matrix[1][2], matrix[2][3], matrix[3][4], matrix[4][5], matrix[5][6], matrix[6][7], matrix[7][8], matrix[8][9]],
        [matrix[0][2], matrix[1][3], matrix[2][4], matrix[3][5], matrix[4][6], matrix[5][7], matrix[6][8], matrix[7][9]],
        [matrix[0][3], matrix[1][4], matrix[2][5], matrix[3][6], matrix[4][7], matrix[5][8], matrix[6][9]],
        [matrix[0][4], matrix[1][5], matrix[2][6], matrix[3][7], matrix[4][8], matrix[5][9]],
        [matrix[0][5], matrix[1][6], matrix[2][7], matrix[3][8], matrix[4][9]],
        [matrix[1][0], matrix[2][1], matrix[3][2], matrix[4][3], matrix[5][4], matrix[6][5], matrix[7][6], matrix[8][7], matrix[9][8]],
        [matrix[2][0], matrix[3][1], matrix[4][2], matrix[5][3], matrix[6][4], matrix[7][5], matrix[8][6], matrix[9][7]],
        [matrix[3][0], matrix[4][1], matrix[5][2], matrix[6][3], matrix[7][4], matrix[8][5], matrix[9][6]],
        [matrix[4][0], matrix[5][1], matrix[6][2], matrix[7][3], matrix[8][4], matrix[9][5]],
        [matrix[5][0], matrix[6][1], matrix[7][2], matrix[8][3], matrix[9][4]],
    ]
    for line in lines:
        for exp in variants:
            if exp in ''.join(line):
                return True
    return False


matrix = []
for i in range(10):
    matrix.append(input())
if is_win(matrix):
    print('YES')
else:
    print('NO')
