from math import floor
from decimal import Decimal
a, b = input().split()
a = int(a)
b = Decimal(b)
print(floor(a * b))
