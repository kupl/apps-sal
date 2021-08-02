field = [['.'] * 9 for i in range(9)]

for i in range(9):
    s = input().split()

    if (s == []):
        s = input().split()

    for j in range(3):
        field[i][3 * j] = s[j][0]
        field[i][3 * j + 1] = s[j][1]
        field[i][3 * j + 2] = s[j][2]

x, y = map(int, input().split())
x -= 1
y -= 1

ix, iy = x % 3, y % 3

if (ix == 0 and iy == 0):
    fl = 0

    for i in range(3):
        for j in range(3):
            if (field[i][j] == '.'):
                fl = 1
                field[i][j] = '!'

    if (not fl):
        for i in range(9):
            for j in range(9):
                if (field[i][j] == '.'):
                    field[i][j] = '!'

if (ix == 0 and iy == 1):
    fl = 0

    for i in range(3):
        for j in range(3, 6):
            if (field[i][j] == '.'):
                fl = 1
                field[i][j] = '!'

    if (not fl):
        for i in range(9):
            for j in range(9):
                if (field[i][j] == '.'):
                    field[i][j] = '!'

if (ix == 0 and iy == 2):
    fl = 0

    for i in range(3):
        for j in range(6, 9):
            if (field[i][j] == '.'):
                fl = 1
                field[i][j] = '!'

    if (not fl):
        for i in range(9):
            for j in range(9):
                if (field[i][j] == '.'):
                    field[i][j] = '!'


if (ix == 1 and iy == 0):
    fl = 0

    for i in range(3, 6):
        for j in range(3):
            if (field[i][j] == '.'):
                fl = 1
                field[i][j] = '!'

    if (not fl):
        for i in range(9):
            for j in range(9):
                if (field[i][j] == '.'):
                    field[i][j] = '!'

if (ix == 1 and iy == 1):
    fl = 0

    for i in range(3, 6):
        for j in range(3, 6):
            if (field[i][j] == '.'):
                fl = 1
                field[i][j] = '!'

    if (not fl):
        for i in range(9):
            for j in range(9):
                if (field[i][j] == '.'):
                    field[i][j] = '!'

if (ix == 1 and iy == 2):
    fl = 0

    for i in range(3, 6):
        for j in range(6, 9):
            if (field[i][j] == '.'):
                fl = 1
                field[i][j] = '!'

    if (not fl):
        for i in range(9):
            for j in range(9):
                if (field[i][j] == '.'):
                    field[i][j] = '!'


if (ix == 2 and iy == 0):
    fl = 0

    for i in range(6, 9):
        for j in range(3):
            if (field[i][j] == '.'):
                fl = 1
                field[i][j] = '!'

    if (not fl):
        for i in range(9):
            for j in range(9):
                if (field[i][j] == '.'):
                    field[i][j] = '!'

if (ix == 2 and iy == 1):
    fl = 0

    for i in range(6, 9):
        for j in range(3, 6):
            if (field[i][j] == '.'):
                fl = 1
                field[i][j] = '!'

    if (not fl):
        for i in range(9):
            for j in range(9):
                if (field[i][j] == '.'):
                    field[i][j] = '!'

if (ix == 2 and iy == 2):
    fl = 0

    for i in range(6, 9):
        for j in range(6, 9):
            if (field[i][j] == '.'):
                fl = 1
                field[i][j] = '!'

    if (not fl):
        for i in range(9):
            for j in range(9):
                if (field[i][j] == '.'):
                    field[i][j] = '!'


for i in range(9):
    if (i % 3 == 0 and i != 0):
        print()

    for j in range(9):
        if (j % 3 == 0 and j != 0):
            print(" ", end="")
        print(field[i][j], end="")

    print()
