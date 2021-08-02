n, t = list(map(int, input().split()))
ot = 0
a = []
b = []
c = []
for i in range(n + 1):
    a.append([])
    b.append([])
    c.append([])
    for j in range(n + 1):
        a[i].append(0)
        b[i].append(0)
        c[i].append(0)
for ii in range(1, t + 1):
    a[0][0] += 1
    if (ot >= (n * n + n) // 2):
        break
    for i in range(n):
        for j in range(i + 1):
            if a[i][j] >= 1:
                if not(c[i][j]):
                    ot += 1
                c[i][j] = 1
                b[i][j] = a[i][j] - 1
                a[i][j] = 1
                a[i + 1][j] += b[i][j] / 2
                b[i][j] = b[i][j] / 2 * 2
                a[i + 1][j + 1] += b[i][j] / 2
                b[i][j] = 0
print(ot)
