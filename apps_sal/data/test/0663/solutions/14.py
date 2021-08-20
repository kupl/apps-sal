import decimal
import math
(r, x, y, x1, y1) = map(decimal.Decimal, input().split())
r *= decimal.Decimal('2')
R = ((x - x1) ** 2 + (y - y1) ** 2) ** decimal.Decimal('0.5')
eps = decimal.Decimal('0.000000001')
print(math.floor((R + r - eps) / r))
