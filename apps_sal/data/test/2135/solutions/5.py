h, w = list(map(int, input().split()))
t = []
for i in range(h):
    lis = input()
    t.append(lis)
a = [[0 for i in range(w)] for j in range(h)]
for i in range(h):
    maxi = 0
    for j in range(1, w):
        if t[i][j] == '.' == t[i][j - 1]:
            a[i][j] = maxi + 1
            maxi = max(maxi, a[i][j])
        else:
            a[i][j] = maxi
d = [[0 for i in range(w)] for j in range(h)]
for i in range(w):
    d[0][i] = a[0][i]
for i in range(1, h):
    for j in range(w):
        d[i][j] = d[i - 1][j] + a[i][j]

a = [[0 for i in range(w)] for j in range(h)]
for j in range(w):
    maxi = 0
    for i in range(1, h):
        if t[i][j] == '.' == t[i - 1][j]:
            a[i][j] = maxi + 1
            maxi = max(maxi, a[i][j])
        else:
            a[i][j] = maxi
d1 = [[0 for i in range(w)] for j in range(h)]
for i in range(h):
    d1[i][0] = a[i][0]
for j in range(1, w):
    for i in range(h):
        d1[i][j] = a[i][j] + d1[i][j - 1]
q = int(input())
for i in range(q):
    r1, c1, r2, c2 = list(map(int, input().split()))
    r1 -= 1
    c1 -= 1
    r2 -= 1
    c2 -= 1
    if r1 == 0 and c1 == 0:
        print(d[r2][c2] + d1[r2][c2])
    elif r1 == 0:
        print(d[r2][c2] + d1[r2][c2] - d[r2][c1] - d1[r2][c1 - 1])
    elif c1 == 0:
        print(d[r2][c2] + d1[r2][c2] - d[r1 - 1][c2] - d1[r1][c2])
    else:
        print(d[r2][c2] + d1[r2][c2] - d[r1 - 1][c2] - d1[r1][c2] - d[r2][c1] - d1[r2][c1 - 1] + d[r1 - 1][c1] + d1[r1][c1 - 1])
