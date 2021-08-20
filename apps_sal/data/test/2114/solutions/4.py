n = int(input())
a = [[0 for j in range(n)] for i in range(n)]
z = 1


def prt(a, n):
    for i in range(n):
        print(*a[i])


if n == 3:
    a = [[7, 1, 9], [8, 6, 5], [3, 2, 4]]
    prt(a, n)
elif n < 4:
    print(-1)
elif n == 4:
    a[0] = [1, 2, 3, 4]
elif n % 2 == 1:
    for i in range(n - 3):
        for j in range(n):
            if i % 2 == 0:
                a[i][j] = z
            else:
                a[i][n - j - 1] = z
            z += 1
    a[n - 1][0] = z
    z += 1
    a[n - 2][0] = z
    z += 1
    a[n - 3][0] = z
    z += 1
    for j in range(1, n - 4):
        a[n - 3][j] = z
        z += 1
        a[n - 2][j] = z
        z += 1
        a[n - 1][j] = z
        z += 1
        if j % 2 == 1:
            (a[n - 3][j], a[n - 1][j]) = (a[n - 1][j], a[n - 3][j])
elif n % 2 == 0:
    for i in range(n - 3):
        for j in range(n):
            if i % 2 == 1:
                a[i][j] = z
            else:
                a[i][n - j - 1] = z
            z += 1
    for j in range(n - 4):
        a[n - 3][j] = z
        z += 1
        a[n - 2][j] = z
        z += 1
        a[n - 1][j] = z
        z += 1
        if j % 2 == 1:
            (a[n - 3][j], a[n - 1][j]) = (a[n - 1][j], a[n - 3][j])
if n >= 4:
    m = n ** 2
    a[n - 3][n - 4] = m - 6
    a[n - 3][n - 3] = m - 5
    a[n - 3][n - 2] = m - 10
    a[n - 3][n - 1] = m - 11
    a[n - 2][n - 4] = m - 8
    a[n - 2][n - 3] = m
    a[n - 2][n - 2] = m - 9
    a[n - 2][n - 1] = m - 2
    a[n - 1][n - 4] = m - 7
    a[n - 1][n - 3] = m - 4
    a[n - 1][n - 2] = m - 3
    a[n - 1][n - 1] = m - 1
    prt(a, n)
