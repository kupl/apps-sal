from math import log
from decimal import Decimal
output = ['x^y^z', 'x^z^y', '(x^y)^z', '(x^z)^y)', 'y^x^z', 'y^z^x', '(y^x)^z', '(y^z)^x', 'z^x^y', 'z^y^x', '(z^x)^y', '(z^y)^x']
(x, y, z) = list(map(Decimal, input().split()))
val = [(Decimal(log(x)) * y ** z, 0), (Decimal(log(x)) * z ** y, -1), (Decimal(log(x)) * (y * z), -2), (Decimal(log(x)) * y ** z, -3), (Decimal(log(y)) * x ** z, -4), (Decimal(log(y)) * z ** x, -5), (Decimal(log(y)) * (x * z), -6), (Decimal(log(y)) * (x * z), -7), (Decimal(log(z)) * x ** y, -8), (Decimal(log(z)) * y ** x, -9), (Decimal(log(z)) * (x * y), -10), (Decimal(log(z)) * (x * y), -11)]
print(output[-max(val)[1]])
