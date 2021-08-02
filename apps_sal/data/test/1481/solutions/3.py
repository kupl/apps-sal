import sys


def o_s(i, j):
    ret = 0
    if board[i - 1][j] == 'o': ret += 1
    if board[i + 1][j] == 'o': ret += 1
    if board[i][j - 1] == 'o': ret += 1
    if board[i][j + 1] == 'o': ret += 1
    return ret


n = int(sys.stdin.readline())
board = ['x' * (n + 2)]
for i in range(n): board.append('x' + sys.stdin.readline().strip() + 'x')
board.append('x' * (n + 2))

even = True
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if o_s(i, j) % 2 == 1: even = False
        if not even: break
    if not even: break
if even: print("YES")
else: print("NO")
