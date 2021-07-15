T = int(input())

for t in range(T):
    N, M = [int(_) for _ in input().split()]
    matrix = []

    for i in range(N):
        row = [int(_) for _ in input().split()]
        matrix.append(row)

    available_rows = 0
    for row in matrix:
        if 1 not in row:
            available_rows += 1
    available_cols = 0
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            if matrix[j][i] == 1:
                break
        else:
            available_cols += 1

    a = min(available_cols, available_rows)
    if a & 1:
        print('Ashish')
    else:
        print('Vivek')

