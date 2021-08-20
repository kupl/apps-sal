tcs = int(input())
board = [['.'] * (tcs + 2)] + [['.'] + [x for x in input()] + ['.'] for i in range(tcs)] + [['.'] * (tcs + 2)]


def do(board, size):
    for i in range(1, size + 1):
        for j in range(1, size + 1):
            listx = [board[i + 1][j], board[i - 1][j], board[i][j - 1], board[i][j + 1]]
            if listx.count('o') % 2 != 0:
                return False
    return True


if do(board, tcs):
    print('YES')
else:
    print('NO')
