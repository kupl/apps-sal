import math
from decimal import Decimal


def sum2(s, e):
    return sum1(e) - sum1(s - 1) - (e - s)


def sum1(i):
    return i * (i + 1) / 2


(n, k) = map(Decimal, input().split())
if n == 1:
    print(0)
elif k > n:
    print(1)
elif sum2(Decimal(2), k) < n:
    print(-1)
else:
    c = 2 * n + k - k * k
    discriminant = (9 - 4 * c).sqrt()
    res1 = math.floor((3 + discriminant) / 2)
    res2 = math.floor((3 - discriminant) / 2)
    res1 = max(res1, res2)
    print(k - res1 + 1)
