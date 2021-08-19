from math import log
from decimal import Decimal
(x, y, z) = [Decimal(x) for x in input().split()]
variants = sorted([(y ** z * Decimal(log(x)), -1), (z ** y * Decimal(log(x)), -2), (y * z * Decimal(log(x)), -3), (x ** z * Decimal(log(y)), -5), (z ** x * Decimal(log(y)), -6), (x * z * Decimal(log(y)), -7), (x ** y * Decimal(log(z)), -9), (y ** x * Decimal(log(z)), -10), (x * y * Decimal(log(z)), -11)])
expressions = ['x^y^z', 'x^z^y', '(x^y)^z', '(x^z)^y', 'y^x^z', 'y^z^x', '(y^x)^z', '(y^z)^x', 'z^x^y', 'z^y^x', '(z^x)^y', '(z^y)^x']
print(expressions[abs(variants[-1][1]) - 1])
