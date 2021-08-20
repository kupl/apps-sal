[n, H] = list(map(int, input().strip().split()))


def bsearch(f, xmin, xmax):
    while xmax - xmin > 1:
        xmid = (xmax + xmin) // 2
        if f(xmid):
            xmax = xmid
        else:
            xmin = xmid
    return xmax


def f1(x):
    return 2 * n <= x * (x + 1)


HH = H * (H + 1) // 2


def f2(x):
    r = x - H
    R0 = r // 2
    R1 = (r + 1) // 2
    return n <= HH + H * r + R0 * R1


if n <= HH:
    x = bsearch(f1, 0, H)
else:
    xmin = H
    xmax = H
    while not f2(xmax):
        xmin = xmax
        xmax *= 2
    x = bsearch(f2, xmin, xmax)
print(x)
