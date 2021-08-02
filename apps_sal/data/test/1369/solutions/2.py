n = int(input())
XY = [tuple(map(int, input().split())) for _ in range(n)]


def f(x, y):
    r = 0
    for xi, yi in XY:
        d = ((x - xi)**2 + (y - yi)**2)**0.5
        if d > r:
            r = d
    return r


def g(x):
    l, r = 0, 1000
    for _ in range(75):
        c1, c2 = (2 * l + r) / 3, (l + 2 * r) / 3
        if f(x, c1) > f(x, c2):
            l = c1
        else:
            r = c2
    return f(x, l)


l, r = 0, 1000
for _ in range(75):
    c1, c2 = (2 * l + r) / 3, (l + 2 * r) / 3
    if g(c1) > g(c2):
        l = c1
    else:
        r = c2

print((g(l)))
