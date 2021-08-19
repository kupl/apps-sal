import math
from decimal import *
(n, a) = map(int, input().split())
d = Decimal(180 / n)
res = Decimal(181)
for i in range(1, n - 1):
    min = abs(Decimal(a - d * i))
    if min < res:
        res = min
        k = i + 2
print('2 1 ', k, sep='')
