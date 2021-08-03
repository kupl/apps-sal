field = []
for i in range(3):
    a1, a2, a3 = [], [], []
    for j in range(3):
        s = list(input())
        a1.append(s[:3])
        a2.append(s[4:7])
        a3.append(s[8:11])
    if i != 2:
        s = input()
    row = [a1, a2, a3]
    field.append(row)
x, y = map(int, input().split())
x -= 1
y -= 1
x, y = x % 3, y % 3
isset = False
for i in range(3):
    for j in range(3):
        if field[x][y][i][j] == '.':
            isset = True
            field[x][y][i][j] = '!'
if not isset:
    for x in range(3):
        for y in range(3):
            for i in range(3):
                for j in range(3):
                    if field[x][y][i][j] == '.':
                        field[x][y][i][j] = '!'
for i in range(3):
    for j in range(3):
        for k in range(3):
            print(*field[i][k][j], sep='', end=' ')
        print()
    print()
