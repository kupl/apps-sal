from math import ceil
s = [list(input().replace(' ', '')) for i in range(3)]
input()
s += [list(input().replace(' ', '')) for i in range(3)]
input()
s += [list(input().replace(' ', '')) for i in range(3)]
(y, x) = [int(k) for k in input().split(' ') if k]
(yb, xb) = (ceil(y / 3), ceil(x / 3))
y -= (yb - 1) * 3 + 1
x -= (xb - 1) * 3 + 1
y *= 3
x *= 3
found = 0
for dy in range(3):
    for dx in range(3):
        if s[y + dy][x + dx] == '.':
            found = 1
            s[y + dy][x + dx] = '!'
if not found:
    for y in range(9):
        for x in range(9):
            if s[y][x] == '.':
                s[y][x] = '!'
for y in range(3):
    for x in range(3):
        print(s[y][x], end='')
    print(' ', end='')
    for x in range(3, 6):
        print(s[y][x], end='')
    print(' ', end='')
    for x in range(6, 9):
        print(s[y][x], end='')
    print(' ')
print()
for y in range(3, 6):
    for x in range(3):
        print(s[y][x], end='')
    print(' ', end='')
    for x in range(3, 6):
        print(s[y][x], end='')
    print(' ', end='')
    for x in range(6, 9):
        print(s[y][x], end='')
    print(' ')
print()
for y in range(6, 9):
    for x in range(3):
        print(s[y][x], end='')
    print(' ', end='')
    for x in range(3, 6):
        print(s[y][x], end='')
    print(' ', end='')
    for x in range(6, 9):
        print(s[y][x], end='')
    print(' ')
