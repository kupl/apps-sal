from decimal import *
from math import sqrt


def __starting_point():
    getcontext().prec = 50
    (a, b, c) = map(Decimal, input().split())
    d = Decimal(sqrt(b * b - 4 * a * c))
    res1 = (d - b) / (2 * a)
    res2 = (-d - b) / (2 * a)
    print(max(res1, res2))
    print(min(res1, res2))


__starting_point()
