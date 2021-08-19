from decimal import Decimal
from decimal import ROUND_FLOOR
(A, B) = [Decimal(i) for i in input().split()]
print((A * B).quantize(Decimal(0), rounding=ROUND_FLOOR))
