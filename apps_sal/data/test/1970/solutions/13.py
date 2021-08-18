def check():
    board = []
    for cont in range(0, 8):
        board.append(input())
    l = True
    for cont in range(0, 8):
        for cont2 in range(0, 8):
            if board[cont][cont2] == 'K':
                if l:
                    xk1 = cont2
                    yk1 = cont
                    l = False
                else:
                    xk2 = cont2
                    yk2 = cont
                    break
    for cont in range(0, 8):
        for cont2 in range(0, 8):
            if cont2 % 2 == xk1 % 2 == xk2 % 2:
                if cont % 2 == yk1 % 2 == yk2 % 2:
                    if abs(cont2 - xk1) % 4 == abs(cont2 - xk2) % 4:
                        if abs(cont - yk1) % 4 == abs(cont - yk2) % 4:
                            if board[cont][cont2] != '
                            print('YES')
                            return
    print('NO')
    return


n = int(input())
check()
for t in range(0, n - 1):
    a = str(input())
    check()
