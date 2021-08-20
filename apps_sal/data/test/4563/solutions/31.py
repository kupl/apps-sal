import math
from fractions import Fraction
from decimal import *
n = int(input())
(x, y) = list(map(int, input().split()))
(t, a) = (x, y)
for _ in range(n - 1):
    (tt, aa) = list(map(int, input().split()))
    '\n    if (t >= a):\n        c = math.ceil(tt / t)\n\n    else:\n        c = math.ceil(aa / a)\n    '
    c = max(math.ceil(Fraction(t, tt)), math.ceil(Fraction(a, aa)))
    c = max(1, c)
    t = tt * c
    a = aa * c
ans = t + a
print(ans)
