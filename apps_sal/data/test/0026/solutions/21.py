from math import log
from decimal import *
(x, y, z) = map(Decimal, input().split())


def logd(x):
    return Decimal(log(x))


r = sorted([(-logd(x) * y ** z, 'x^y^z'), (-logd(x) * z ** y, 'x^z^y'), (-logd(x) * y * z, '(x^y)^z'), (-logd(y) * x ** z, 'y^x^z'), (-logd(y) * z ** x, 'y^z^x'), (-logd(y) * z * x, '(y^x)^z'), (-logd(z) * x ** y, 'z^x^y'), (-logd(z) * y ** x, 'z^y^x'), (-logd(z) * x * y, '(z^x)^y')], key=lambda a: a[0])
print(r[0][1])
