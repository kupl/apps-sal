def check(a, b, c, d, e):
    countX = 0
    countD = 0
    if a == 'X':
        countX += 1
    elif a == '.':
        countD += 1
    if b == 'X':
        countX += 1
    elif b == '.':
        countD += 1
    if c == 'X':
        countX += 1
    elif c == '.':
        countD += 1
    if d == 'X':
        countX += 1
    elif d == '.':
        countD += 1
    if e == 'X':
        countX += 1
    elif e == '.':
        countD += 1
    return countX == 4 and countD == 1


def f(a):
    for i in range(10):
        for j in range(6):
            if check(a[i][j], a[i][j + 1], a[i][j + 2], a[i][j + 3], a[i][j + 4]) or (i < 6 and check(a[i][j], a[i + 1][j + 1], a[i + 2][j + 2], a[i + 3][j + 3], a[i + 4][j + 4])):
                return True
    for i in range(10):
        for j in range(6):
            if check(a[j][i], a[j + 1][i], a[j + 2][i], a[j + 3][i], a[j + 4][i]) or (i > 3 and check(a[j][i], a[j + 1][i - 1], a[j + 2][i - 2], a[j + 3][i - 3], a[j + 4][i - 4])):
                return True


print('YES' if f([input() for _ in range(10)]) else 'NO')
