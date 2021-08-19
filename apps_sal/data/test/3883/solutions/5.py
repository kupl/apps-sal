from decimal import *
import math
getcontext().prec = 50
(a, b) = map(Decimal, input().split())
print(-1 if b > a else Decimal((a + b) / 2) / math.floor(Decimal((a + b) / 2) / b))
