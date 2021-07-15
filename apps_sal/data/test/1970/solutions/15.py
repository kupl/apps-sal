n = int(input())
for t in range(n):
    if t: input()
    board = [[c for c in input()] for i in range(8)]
    k1, k2 = ((i, j) for i in range(8) for j in range(8) if board[i][j] == 'K')
    if (k1[0] - k2[0]) % 4 == 0 and (k1[1] - k2[1]) % 4 == 0:
        print('YES')
    else:
        print('NO')




