x, y, x0, y0 = [int(x) for x in input().split()]
x0 -= 1
y0 -= 1
commands = input()
xy = x * y
l = len(commands)
a = [0] * (l + 1)
n = 0
field = [[-1] * y for i in range(x)]
field[x0][y0] = 0
for i in range(l):
    command = commands[i]
    if command == 'U':
        if x0 > 0:
            x0 -= 1
    elif command == 'D':
        if x0 + 1 < x:
            x0 += 1
    elif command == 'L':
        if y0 > 0:
            y0 -= 1
    elif command == 'R':
        if y0 + 1 < y:
            y0 += 1
    if field[x0][y0] < 0:
        field[x0][y0] = i + 1
for i in range(x):
    for j in range(y):
        a[field[i][j]] += 1
print(' '.join(str(x) for x in a))
