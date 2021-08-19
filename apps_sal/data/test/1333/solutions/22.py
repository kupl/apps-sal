def printBoard(res):
    for i in range(0, len(res)):
        print("".join(res[i]))


n, m = [int(x) for x in input().strip().split()]

res = [["."] * m for i in range(0, n)]

for i in range(0, n, 2):

    for j in range(0, m):
        res[i][j] = "#"
    if i + 1 < n:
        if (i + 1) % 4 == 1:
            res[i + 1][m - 1] = "#"
        elif (i + 1) % 4 == 3:
            res[i + 1][0] = "#"

printBoard(res)
