import math
import decimal
output = ['x^y^z', 'x^z^y', '(x^y)^z', '(x^z)^y', 'y^x^z', 'y^z^x', '(y^x)^z', '(y^z)^x', 'z^x^y', 'z^y^x', '(z^x)^y', '(z^y)^x']
(x, y, z) = map(decimal.Decimal, input().split())
a = []
a += [(decimal.Decimal(math.log(x)) * y ** z, 0)]
a += [(decimal.Decimal(math.log(x)) * z ** y, -1)]
a += [(decimal.Decimal(math.log(x)) * y * z, -2)]
a += [(decimal.Decimal(math.log(y)) * x ** z, -4)]
a += [(decimal.Decimal(math.log(y)) * z ** x, -5)]
a += [(decimal.Decimal(math.log(y)) * x * z, -6)]
a += [(decimal.Decimal(math.log(z)) * x ** y, -8)]
a += [(decimal.Decimal(math.log(z)) * y ** x, -9)]
a += [(decimal.Decimal(math.log(z)) * x * y, -10)]
print(output[-max(a)[1]])
