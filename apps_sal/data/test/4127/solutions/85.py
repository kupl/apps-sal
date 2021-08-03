from decimal import Decimal
from math import floor
a, b = map(Decimal, input().split())
print(floor(a * b))
