from decimal import *
from math import log


def d_log(x):
    return Decimal(log(x))


def __starting_point():

    x, y, z = map(Decimal, input().split())
    exps = [((y**z) * d_log(x), 0),
            ((z**y) * d_log(x), 1),
            (z * y * d_log(x), 2),
            ((x**z) * d_log(y), 4),
            ((z**x) * d_log(y), 5),
            (z * x * d_log(y), 6),
            ((x**y) * d_log(z), 8),
            ((y**x) * d_log(z), 9),
            (y * x * d_log(z), 10),
            ]

    exps.sort(key=lambda e: (-e[0], e[1]))

    c = exps[0][1]

    res = ["x^y^z", "x^z^y", "(x^y)^z", "(x^z)^y",
           "y^x^z", "y^z^x", "(y^x)^z", "(y^z)^x",
           "z^x^y", "z^y^x", "(z^x)^y", "(z^y)^x"
           ]
    print(res[c])


__starting_point()
