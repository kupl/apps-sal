from math import log
from decimal import Decimal


def t1(a, b, c):
    return int((Decimal(log(a)) * (b ** c)) / Decimal(0.000000000001))


def t2(a, b, c):
    return int((Decimal(log(a)) * b * c) / Decimal(0.000000000001))


def solve():
    x, y, z = list(map(Decimal, input().split()))

    a = [0.0] * 12

    a[0] = t1(x, y, z), 0, 'x^y^z'
    a[1] = t1(x, z, y), -1, 'x^z^y'
    a[2] = t2(x, y, z), -2, '(x^y)^z'
    a[3] = t2(x, z, y), -3, '(x^z)^y'

    a[4] = t1(y, x, z), -4, 'y^x^z'
    a[5] = t1(y, z, x), -5, 'y^z^x'
    a[6] = t2(y, x, z), -6, '(y^x)^z'
    a[7] = t2(y, z, x), -7, '(y^z)^x'

    a[8] = t1(z, x, y), -8, 'z^x^y'
    a[9] = t1(z, y, x), -9, 'z^y^x'
    a[10] = t2(z, x, y), -10, '(z^x)^y'
    a[11] = t2(z, y, x), -11, '(z^y)^x'

    v, i, f = max(a)

    print(f)


def __starting_point():
    solve()


__starting_point()
