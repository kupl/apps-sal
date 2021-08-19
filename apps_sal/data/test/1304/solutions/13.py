a = [[[['.'] * 3 for i in range(3)] for i in range(3)] for i in range(3)]
for i in range(3):
    s = input().split()
    for j in range(3):
        for h in range(3):
            ch = s[j][h]
            a[0][j][i][h] = ch
x = input()
for i in range(3):
    s = input().split()
    for j in range(3):
        for h in range(3):
            ch = s[j][h]
            a[1][j][i][h] = ch
x = input()
for i in range(3):
    s = input().split()
    for j in range(3):
        for h in range(3):
            ch = s[j][h]
            a[2][j][i][h] = ch
(x, y) = map(int, input().split())
x = x % 3 - 1
y = y % 3 - 1
fl = True
for i in range(3):
    for j in range(3):
        if a[x][y][i][j] == '.':
            fl = False
            a[x][y][i][j] = '!'
if fl:
    for x in range(3):
        for y in range(3):
            for i in range(3):
                for j in range(3):
                    if a[x][y][i][j] == '.':
                        a[x][y][i][j] = '!'
for i in range(3):
    for j in range(3):
        print(*a[0][j][i], sep='', end=' ')
    print()
print()
for i in range(3):
    for j in range(3):
        print(*a[1][j][i], sep='', end=' ')
    print()
print()
for i in range(3):
    for j in range(3):
        print(*a[2][j][i], sep='', end=' ')
    print()
