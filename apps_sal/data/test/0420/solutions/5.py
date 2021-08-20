(n, m) = map(int, input().split())
matrix = []
for i in range(n):
    matrix.append([int(x) for x in input().split()])


def mirror(matrix):
    mirrormatrix = matrix[:]
    matrix.reverse()
    mirrormatrix += matrix[:]
    matrix.reverse()
    return mirrormatrix


while True:
    if len(matrix) % 2 == 0:
        if mirror(matrix[:int(len(matrix) / 2)]) == matrix:
            matrix = matrix[:int(len(matrix) / 2)]
        else:
            print(len(matrix))
            break
    else:
        print(len(matrix))
        break
