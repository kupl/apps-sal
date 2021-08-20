a = [[] for i in range(10)]
pp = -1
for i in range(11):
    b = input()
    b.split()
    if i == 3 or i == 7:
        continue
    pp += 1
    for j in range(len(b)):
        if b[j] == ' ':
            continue
        a[pp].append(b[j])
(x, y) = map(int, input().split())
x %= 3
y %= 3
if x == 0:
    x0 = 6
if x == 1:
    x0 = 0
if x == 2:
    x0 = 3
if y == 0:
    y0 = 6
if y == 1:
    y0 = 0
if y == 2:
    y0 = 3
ans = False
for i in range(x0, x0 + 3):
    for j in range(y0, y0 + 3):
        if a[i][j] == '.':
            ans = True
            a[i][j] = '!'
if ans == False:
    for i in range(0, 9):
        for j in range(0, 9):
            if a[i][j] == '.':
                a[i][j] = '!'
for i in range(0, 9):
    if i == 3 or i == 6:
        print()
    for j in range(0, 9):
        if j == 3 or j == 6:
            print(end=' ')
        print(a[i][j], end='')
    print()
