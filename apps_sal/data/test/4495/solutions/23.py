import math
from decimal import *

a, b, x = map(Decimal, input().split())

print(max(0, (b // x) - math.ceil(a / x) + 1))
