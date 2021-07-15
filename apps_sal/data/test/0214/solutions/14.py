

A = []
A += [input()]
A += [input()]

n = len(A[0])

B = [[0 for _ in range(4)] for _ in range(n + 1)]

B[0][0] = -1000
B[0][1] = -1000
B[0][2] = -1000
B[0][3] = 0

for i in range(1, n + 1):
    # 0
    if A[1][i - 1] == 'X':
        B[i][0] = -1000
    elif A[0][i - 1] == 'X':
        B[i][0] = max([B[i - 1][j] for j in range(4)])
    else:
        B[i][0] = max([B[i - 1][2] + 1] + [B[i - 1][0],
                                           B[i - 1][1], B[i - 1][3]])

    # 1
    if A[0][i - 1] == 'X':
        B[i][1] = -1000
    elif A[1][i - 1] == 'X':
        B[i][1] = max([B[i - 1][j] for j in range(4)])
    else:
        B[i][1] = max([B[i - 1][2] + 1] + [B[i - 1][0],
                                           B[i - 1][1], B[i - 1][3]])

    # 3
    if A[0][i - 1] == 'X' or A[1][i - 1] == 'X':
        B[i][2] = -1000
    else:
        B[i][2] = max([B[i - 1][j] for j in range(4)])

    # 4
    if A[0][i - 1] == 'X' and A[1][i - 1] == 'X':
        B[i][3] = max([B[i - 1][j] for j in range(4)])
    elif A[0][i - 1] == 'X':
        B[i][3] = B[i - 1][2] + 1
    elif A[1][i - 1] == 'X':
        B[i][3] = B[i - 1][2] + 1
    else:
        B[i][3] = max([B[i - 1][j] for j in range(3)]) + 1



print(max([B[n][j] for j in range(4)]))

