n = int(input())
board = [list(input()) for _ in range(n)]

def f(i, j):
    if j == 0 or j == n - 1:
        return False
    if i >= n - 2:
        return False
    if '#' in (board[i + 1][j - 1], board[i + 1][j], board[i + 1][j + 1], board[i + 2][j]):
        return False
    return True

def g(i, j):
    board[i][j] = '#'
    board[i + 1][j - 1] = '#'
    board[i + 1][j] = '#'
    board[i + 1][j + 1] = '#'
    board[i + 2][j] = '#'

for i in range(n):
    for j in range(n):
        if board[i][j] == '.':
            if not f(i, j):
                print('NO')
                return
            g(i, j)

print('YES')

