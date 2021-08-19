from math import sqrt
n = int(input())
xy = [[int(i) for i in input().split()] for _ in range(n)]


def d(x, y):
    return sqrt((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2)


def nai(x, y, z):
    (c, b, a) = sorted([d(x, y), d(y, z), d(z, x)])
    co = (b ** 2 + c ** 2 - a ** 2) / (2 * b * c)
    if co < 0:
        return a / 2
    si = sqrt(1 - co ** 2)
    return a / si / 2


if n == 2:
    print(d(xy[0], xy[1]) / 2)
else:
    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                ans = max(ans, nai(xy[i], xy[j], xy[k]))
    print(ans)
