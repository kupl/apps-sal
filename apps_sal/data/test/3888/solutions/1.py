def mex(x, y):
    if x * y > 0:
        return 0
    elif x == 1 and y == 0:
        return 2
    elif x == 0 and y == 1:
        return 2
    else:
        return 1


"\nimport random\n\nN = 15\nmatrix = []\nfor i in range(N):\n    matrix.append([7] * N)\n\nfor i in range(N):\n    matrix[0][i] = random.randint(0,2)\nfor j in range(1, N):\n    matrix[j][0] = random.randint(0,2)\n\nfor i in range(N):\n    print(matrix[i])\n\n\n\n\n\nfor i in range(1, N):\n    for j in range(1, N):\n        matrix[i][j] = mex(matrix[i-1][j], matrix[i][j-1])\n\nprint('~~~~~~~~~~~~~~~~~~~~~~~~~~~')\nfor i in range(N):\n    print(matrix[i])\ngutyoku = [0,0,0]\nfor i in range(N):\n    for j in range(N):\n        gutyoku[matrix[i][j]] += 1\nprint(gutyoku)\n\n\n\nprint('~~~~~~~~~~~~~~~~~~~~~~~+++++++++~~~~~~~~~~~')\n"
counter = [0, 0, 0]
N = int(input())
if N == 1:
    counter[int(input())] += 1
    print('{} {} {}'.format(counter[0], counter[1], counter[2]))
elif N == 2:
    A = list(map(int, input().split()))
    B = int(input())
    counter[A[0]] += 1
    counter[A[1]] += 1
    counter[B] += 1
    counter[mex(A[1], B)] += 1
    print('{} {} {}'.format(counter[0], counter[1], counter[2]))
else:
    A = list(map(int, input().split()))
    B = []
    for i in range(N - 1):
        B.append(int(input()))
    matrix = []
    matrix.append(A)
    for j in range(1, N):
        matrix.append([B[j - 1]])
    for i in range(1, 3):
        for j in range(1, N):
            matrix[i].append(mex(matrix[i - 1][j], matrix[i][j - 1]))
    for i in range(3, N):
        for j in range(1, 3):
            matrix[i].append(mex(matrix[i - 1][j], matrix[i][j - 1]))
    counter = [0, 0, 0]
    for i in range(3):
        for j in range(N):
            counter[matrix[i][j]] += 1
    for i in range(3, N):
        for j in range(3):
            counter[matrix[i][j]] += 1
    for i in range(3, 4):
        for j in range(3, N):
            matrix[i].append(mex(matrix[i - 1][j], matrix[i][j - 1]))
            counter[mex(matrix[i - 1][j], matrix[i][j - 1])] += N - j
    for i in range(4, N):
        for j in range(3, 4):
            matrix[i].append(mex(matrix[i - 1][j], matrix[i][j - 1]))
            counter[mex(matrix[i - 1][j], matrix[i][j - 1])] += N - i
    print('{} {} {}'.format(counter[0], counter[1], counter[2]))
