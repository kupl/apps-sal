import os


def f():
    board = []
    for i in range(10):
        board.append(input())
    for i, row in enumerate(board):
        for j, c in enumerate(row):
            if c == '.':
                d1 = d2 = 0
                b = j - 1
                while b >= 0:
                    if row[b] == 'X':
                        d1 += 1
                        b -= 1
                    else:
                        break
                b = j + 1
                while b <= 9:
                    if row[b] == 'X':
                        d2 += 1
                        b += 1
                    else:
                        break
                if d1 + d2 >= 4:
                    print('YES')
                    return
                d1 = d2 = 0
                a = i - 1
                while a >= 0:
                    if board[a][j] == 'X':
                        d1 += 1
                        a -= 1
                    else:
                        break
                a = i + 1
                while a <= 9:
                    if board[a][j] == 'X':
                        d2 += 1
                        a += 1
                    else:
                        break
                if d1 + d2 >= 4:
                    print('YES')
                    return
                d1 = d2 = 0
                a = i - 1
                b = j - 1
                while a >= 0 and b >= 0:
                    if board[a][b] == 'X':
                        d1 += 1
                        a -= 1
                        b -= 1
                    else:
                        break
                a = i + 1
                b = j + 1
                while a <= 9 and b <= 9:
                    if board[a][b] == 'X':
                        d2 += 1
                        a += 1
                        b += 1
                    else:
                        break
                if d1 + d2 >= 4:
                    print('YES')
                    return
                d1 = d2 = 0
                a = i + 1
                b = j - 1
                while a <= 9 and b >= 0:
                    if board[a][b] == 'X':
                        d1 += 1
                        a += 1
                        b -= 1
                    else:
                        break
                a = i - 1
                b = j + 1
                while a >= 0 and b <= 9:
                    if board[a][b] == 'X':
                        d2 += 1
                        a -= 1
                        b += 1
                    else:
                        break
                if d1 + d2 >= 4:
                    print('YES')
                    return
    print('NO')


f()
