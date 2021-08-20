from fractions import Decimal
import math
n = Decimal(input())
d = Decimal('1')
while n % d == 0:
    d *= 3
if d > n:
    print(1)
else:
    print(math.ceil(n / d))
