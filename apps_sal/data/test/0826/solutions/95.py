import math
from decimal import *
n = int(input())
m = int((-1 + Decimal(1 + 4 * (2 * n + 2)) ** Decimal(0.5)) / 2)

print((n - m + 1))

