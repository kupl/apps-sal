from math import log10
from decimal import Decimal

ans = ["x^y^z", "x^z^y", "(x^y)^z", "(x^z)^y)", "y^x^z", "y^z^x", "(y^x)^z", "(y^z)^x", "z^x^y", "z^y^x", "(z^x)^y", "(z^y)^x"]

x, y, z = list(map(Decimal, input().split()))

val = [ (Decimal(log10(x)) * (y ** z), -0),
        (Decimal(log10(x)) * (z ** y), -1),
        (Decimal(log10(x)) * (y * z), -2),
        (Decimal(log10(x)) * (y ** z), -3),
        (Decimal(log10(y)) * (x ** z), -4),
        (Decimal(log10(y)) * (z ** x), -5),
        (Decimal(log10(y)) * (x * z), -6),
        (Decimal(log10(y)) * (x * z), -7),
        (Decimal(log10(z)) * (x ** y), -8),
        (Decimal(log10(z)) * (y ** x), -9),
        (Decimal(log10(z)) * (x * y), -10),
        (Decimal(log10(z)) * (x * y), -11)
        ]

print(ans[-max(val)[1]])

