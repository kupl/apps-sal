a = [[''] * 9 for i in range(9)]

for i in range(3):
    for j in range(3):
        q = input()
        q = q.replace(' ', '')
        for p in range(9):
            a[i * 3 + j][p] = q[p]
    if i != 2:
        q = input()

x, y = [int(i) for i in input().split()]
x1, y1 = x, y
while x1 > 3:
    x1 -= 3
while y1 > 3:
    y1 -= 3
x1 -= 1
y1 -= 1
ch = False
for i in range(3):
    for j in range(3):
        if a[i + x1 * 3][j + y1 * 3] == '.':
            ch = True
        if ch and a[i + x1 * 3][j + y1 * 3] == '.':
            a[i + x1 * 3][j + y1 * 3] = '!'
if not ch:
    for i in range(9):
        for j in range(9):
            if a[i][j] == '.':
                a[i][j] = '!'
for i in range(3):
    for j in range(3):

        for p in range(3):
            for q in range(3):
                print(a[i * 3 + j][p * 3 + q], end='')
            print(' ', end='')
        print()
    print()
