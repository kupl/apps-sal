import math
from decimal import *
(a, b) = map(str, input().split())
ans = Decimal(a) * Decimal(b) // 1
print(ans)
