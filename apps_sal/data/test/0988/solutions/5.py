def good(i, j):
    x = i // 2
    y = j // 2
    return 3 - x + (y == 1)


b = [0] * 6
for i in range(6):
    b[i] = input().split('-')
    b[i] = [b[i][0][0], b[i][0][1], b[i][1][0], b[i][1][1], b[i][2][0], b[i][2][1]]
mx = 0
mi = 0
mj = 0
for i in range(6):
    for j in range(6):
        if b[i][j] == '.':
            if good(i, j) > mx:
                mx = good(i, j)
                mi = i
                mj = j
b[mi][mj] = 'P'
for i in range(6):
    print(b[i][0] + b[i][1] + '-' + b[i][2] + b[i][3] + '-' + b[i][4] + b[i][5])
