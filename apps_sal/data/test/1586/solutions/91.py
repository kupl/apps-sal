import math
from decimal import *


def cnt_prime(p, n):
    div = Decimal(str(n))
    s = 0
    while True:
        div /= p
        if div < 1:
            break
        if p == 2:
            s += int(div.quantize(Decimal('0.0'), rounding=ROUND_FLOOR))
        else:
            s += int(div.quantize(Decimal('0.0'), rounding=ROUND_FLOOR)) // 2
    return s


N = int(input())
if N % 2 == 1:
    print(0)
else:
    print(min(cnt_prime(2, N), cnt_prime(5, N)))
