def checkFail(i, j):
    if i - 1 >= 0 and j - 1 >= 0:
        res = 0
        for x in range(i - 1, i + 1):
            for y in range(j - 1, j + 1):
                res += board[x][y]
        if res == 4:
            return True
    if i - 1 >= 0 and j + 1 < m:
        res = 0
        for x in range(i - 1, i + 1):
            for y in range(j, j + 2):
                res += board[x][y]
        if res == 4:
            return True
    if i + 1 < n and j - 1 >= 0:
        res = 0
        for x in range(i, i + 2):
            for y in range(j - 1, j + 1):
                res += board[x][y]
        if res == 4:
            return True
    if i + 1 < n and j + 1 < m:
        res = 0
        for x in range(i, i + 2):
            for y in range(j, j + 2):
                res += board[x][y]
        if res == 4:
            return True

    return False


n, m, k = [int(x) for x in input().strip().split()]
board = [[0] * m for i in range(0, n)]

isFail = False
res = 0
for moveIndex in range(0, k):
    i, j = [int(x) for x in input().strip().split()]
    if not isFail:
        i -= 1
        j -= 1
        if board[i][j] == 0:
            board[i][j] = 1
            if checkFail(i, j):
                isFail = True
                res = moveIndex + 1
print(res)
