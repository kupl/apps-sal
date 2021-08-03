import math
n, m = list(map(int, input().split()))

swapped = False
if n > m:
    n, m = m, n
    swapped = True


def mprint(x, y):
    nonlocal swapped
    if swapped:
        print(y, x)
    else:
        print(x, y)


def mlen(pnt):
    res = 0.0
    for i in range(1, 4):
        val = (pnt[i][0] - pnt[i - 1][0]) ** 2
        val += (pnt[i][1] - pnt[i - 1][1]) ** 2
        val = math.sqrt(val)
        res += val
    return res


if n == 0:
    mprint(0, 1)
    mprint(0, m)
    mprint(0, 0)
    mprint(0, m - 1)
else:
    one = [(0, 0), (n, m), (n, 0), (0, m)]
    two = [(1, 0), (n, m), (0, 0), (n - 1, m)]
    if mlen(one) > mlen(two):
        two = one
    for x in two:
        mprint(*x)
