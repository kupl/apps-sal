n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
b = []
for i in range(n):
    b.append([0] * m)


def fill(x, y):
    for i in range(n):
        b[i][y] = 1
    for i in range(m):
        b[x][i] = 1


def getv(c, x, y):
    res = False
    for i in range(n):
        res = res or c[i][y]
    for i in range(m):
        res = res or c[x][i]
    return res


def getv2(c, x, y):
    res = True
    for i in range(n):
        res = res and c[i][y]
    for i in range(m):
        res = res and c[x][i]
    return res


for i in range(n):
    for j in range(m):
        if getv2(a, i, j):
            b[i][j] = 1


good = True
for i in range(n):
    for j in range(m):
        if a[i][j] != getv(b, i, j):
            good = False

if good == False:
    print("NO")
else:
    print("YES")
    for i in range(n):
        for j in range(m - 1):
            print(b[i][j], end=' ')
        print(b[i][m - 1])
