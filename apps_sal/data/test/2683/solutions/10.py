

def checkRow(A, row, N, K):
    count = 0
    move = 0
    for i in range(N):
        if(A[row][i] == '.'):
            move = move + 1
        if(not(A[row][i] == 'O') and move < 2):
            count = count + 1
        elif(A[row][i] == '.'):
            move = 1
            count = 1
        else:
            count = 0
            move = 0
        if(count == K):
            return 1
    return 0


def checkCol(A, col, N, K):
    count = 0
    move = 0
    for i in range(N):
        if(A[i][col] == '.'):
            move = move + 1
        if(not(A[i][col] == 'O') and move < 2):
            count = count + 1
        elif(A[i][col] == '.'):
            count = 1
            move = 1
        else:
            count = 0
            move = 0
        if(count == K):
            return 1
    return 0


def checkDiag(A, row, col, N, K):
    count = 0
    move = 0

    for i in range(K):
        if(A[row + i][col + i] == '.'):
            move = move + 1
        if(A[row + i][col + i] == '0' and move <= 1):
            return 0

    if(move < 2):
        return 1
    return 0


def chck(A, N, K):
    flag = 0

    if(flag == 0):
        for i in range(N):
            flag = checkRow(A, i, N, K)
            if(flag == 1):
                break

    if(flag == 0):
        for j in range(N):
            flag = checkCol(A, j, N, K)
            if(flag == 1):
                break

    if(flag == 0):
        for i in range(N - K + 1):
            for j in range(N - K + 1):
                flag = checkDiag(A, i, j, N, K)
                if(flag == 1):
                    break
            if(flag == 1):
                break

    return flag


for tests in range(eval(input())):
    [N, K] = list(map(int, input().split()))
    A = [""] * N

    for i in range(N):
        A[i] = input()

    if(chck(A, N, K) == 1):
        print("YES")
    else:
        print("NO")
