import math
from decimal import *
a, b = map(str, input().split())
a_ = Decimal(a)
b_ = Decimal(b)
print(math.floor(a_ * b_))
