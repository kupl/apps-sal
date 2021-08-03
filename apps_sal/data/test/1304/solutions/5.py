a = [0] * 9


def check(x, y):
    nonlocal a
    for i in range(3):
        for j in range(3):
            if (a[i + x * 3][j + y * 3] == '.'):
                return True
    return False


def yall():
    nonlocal a
    for i in range(9):
        for j in range(9):
            if (a[i][j] == '.'):
                a[i][j] = '!'


def nall(x, y):
    nonlocal a
    for i in range(3):
        for j in range(3):
            if (a[i + x * 3][j + y * 3] == '.'):
                a[i + x * 3][j + y * 3] = '!'


for i in range(9):
    b = [j for j in input().split()]
    a[i] = [b[k][j] for k in range(3) for j in range(3)]
    if (i % 3 == 2 and i != 8):
        input()

x, y = [int(i) for i in input().split()]
x1 = (x - 1) % 3
y1 = (y - 1) % 3

if check(x1, y1):
    nall(x1, y1)
else:
    yall()

for i in range(9):
    for j in range(9):
        print(a[i][j], end='')
        if (j % 3 == 2):
            print(" ", end='')
    if (i % 3 == 2):
        print()
    print()
