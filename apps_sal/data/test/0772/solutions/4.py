a = [[1] * 3 for i in range(3)]
b = []
for i in range(3):
    b.append(list(map(int, input().split())))

for i in range(3):
    for j in range(3):
        b[i][j] %= 2

        if b[i][j] == 1:
            if i > 0:
                a[i - 1][j] = 1 - a[i - 1][j]
            if i < 2:
                a[i + 1][j] = 1 - a[i + 1][j]
            if j > 0:
                a[i][j - 1] = 1 - a[i][j - 1]
            if j < 2:
                a[i][j + 1] = 1 - a[i][j + 1]
            a[i][j] = 1 - a[i][j]

for i in range(3):
    print('%d%d%d' % (a[i][0], a[i][1], a[i][2]))
