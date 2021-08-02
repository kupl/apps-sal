a = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
d = {0: 1, 1: 0}
for i in range(3):
    b = list(map(int, input().split()))
    for j in range(3):
        if b[j] % 2 == 1:
            a[i][j] = d[a[i][j]]
            if i != 0:
                a[i - 1][j] = d[a[i - 1][j]]
            if i != 2:
                a[i + 1][j] = d[a[i + 1][j]]
            if j != 0:
                a[i][j - 1] = d[a[i][j - 1]]
            if j != 2:
                a[i][j + 1] = d[a[i][j + 1]]
for i in range(3):
    for j in range(3):
        print(a[i][j], end='')
    print()
