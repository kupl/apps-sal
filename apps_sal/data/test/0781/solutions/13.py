board = []
for cont in range(0,8):
    board.append(input())
l = True
for row in board:
    for cont in range(0,7):
        if row[cont] == row[cont+1]:
            l = False
            break
    if l is False:
        break

if l:
    print('YES')
else:
    print('NO')
