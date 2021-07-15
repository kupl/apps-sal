def fits(x, y):
    nonlocal n
    return x >= 0 and x < n and y >= 0 and y < n

def paint(x, y):
    nonlocal a
    a[x][y] = '.'
    a[x - 1][y] = '.'
    a[x + 1][y] = '.'
    a[x][y - 1] = '.'
    a[x][y + 1] = '.'

def check(x, y):
    nonlocal a
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    cnt = 0
    for i in range(4):
        if (fits(x + dx[i], y + dy[i]) and a[x + dx[i]][y + dy[i]] == '#'):
            cnt += 1
    if (a[x][y] == '#'):
        cnt += 1
    if (cnt == 5):
        paint(x, y)

n = int(input())
a = []
for i in range(n):
    a.append(list(input()))
for i in range(n):
    for j in range(n):
        check(i, j)
cnt = 0
for el in a:
    for el2 in el:
        if el2 == '#':
            cnt += 1

if (cnt == 0):
    print('YES')
else:
    print('NO')

