from math import log
from decimal import *
(x, y, z) = map(Decimal, input().split())


def logd(x):
    return Decimal(log(x))


r = [(lambda x, y, z: y ** z * logd(x), 'x^y^z'), (lambda x, y, z: z ** y * logd(x), 'x^z^y'), (lambda x, y, z: logd(x) * y * z, '(x^y)^z'), (lambda x, y, z: logd(y) * x ** z, 'y^x^z'), (lambda x, y, z: logd(y) * z ** x, 'y^z^x'), (lambda x, y, z: logd(y) * z * x, '(y^x)^z'), (lambda x, y, z: logd(z) * x ** y, 'z^x^y'), (lambda x, y, z: logd(z) * y ** x, 'z^y^x'), (lambda x, y, z: logd(z) * x * y, '(z^x)^y')]
exp = ''
best = -10 ** 50
for (f, e) in r:
    val = f(x, y, z)
    if val > best:
        best = val
        exp = e
print(exp)
