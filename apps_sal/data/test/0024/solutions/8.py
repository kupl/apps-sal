a = [0 for i in range(10)]
for i in range(10):
    a[i] = input()
b = [[0 for i in range(10)] for i in range(10)]
f = False
for x1 in range(10):
    for y1 in range(10):
        for i in range(10):
            for j in range(10):
                b[i][j] = a[i][j]
        if b[x1][y1] == '.':
            b[x1][y1] = 'X'
        can = False
        for i in range(10):
            for j in range(10):
                if j < 6 and b[i][j] == 'X' and (b[i][j + 1] == 'X') and (b[i][j + 2] == 'X') and (b[i][j + 3] == 'X') and (b[i][j + 4] == 'X'):
                    can = True
                if i < 6 and b[i][j] == 'X' and (b[i + 1][j] == 'X') and (b[i + 2][j] == 'X') and (b[i + 3][j] == 'X') and (b[i + 4][j] == 'X'):
                    can = True
                if i < 6 and j < 6 and (b[i][j] == 'X') and (b[i + 1][j + 1] == 'X') and (b[i + 2][j + 2] == 'X') and (b[i + 3][j + 3] == 'X') and (b[i + 4][j + 4] == 'X'):
                    can = True
                if i < 6 and j > 3 and (b[i][j] == 'X') and (b[i + 1][j - 1] == 'X') and (b[i + 2][j - 2] == 'X') and (b[i + 3][j - 3] == 'X') and (b[i + 4][j - 4] == 'X'):
                    can = True
        if can == True:
            f = True
if f:
    print('YES')
else:
    print('NO')
