from math import acos
from decimal import *

eps = 2e-7
pi = Decimal('3.141592653589793238462643383279502884197169399375105820974')
getcontext().prec = 40


def _acos(x):
    if 1 - eps > abs(x) > eps:
        return Decimal(acos(x))

    if x < 0:
        return pi - _acos(-x)

    if abs(x) < eps:
        return pi / 2 - x - x**3 / 6 - x**5 * 3 / 40 - x**7 * 5 / 112
    else:
        t = Decimal(1) - x
        return (2 * t).sqrt() * (1 + t / 12 + t**2 * 3 / 160 + t**3 * 5 / 896 + t**4 * 35 / 18432 + t**5 * 63 / 90112);


O1 = [0, 0]
O2 = [0, 0]

O1[0], O1[1], r1 = map(Decimal, input().split())
O2[0], O2[1], r2 = map(Decimal, input().split())

d2 = (O1[0] - O2[0])**2 + (O1[1] - O2[1])**2
ans = 0

if d2 <= (r1 - r2)**2:  # d^2 <= |r1 - r2| -> a circle inside another one
    ans = pi * (min(r1, r2) ** 2)

elif (r1 - r2)**2 < d2 < (r1 + r2)**2:  # 2 circles cut
    kite = (-r1**4 - d2**2 - r2**4 + 2 * (r1 * r1 * d2 + r2 * r2 * d2 + r1 * r1 * r2 * r2)).sqrt()
    d = d2.sqrt()

    alpha1 = _acos((r1**2 + d2 - r2**2) / (2 * r1 * d))
    alpha2 = _acos((r2**2 + d2 - r1**2) / (2 * r2 * d))

    ans = r1**2 * alpha1 + r2**2 * alpha2 - kite / 2

print("%.9f" % ans)
