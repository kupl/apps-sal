from math import gcd, floor, ceil
from random import randrange


def li():
    return list(map(int, input().split()))


(h, m) = li()
(cur, d, c, n) = li()
if 60 * h + m < 20 * 60:
    an = (cur + n - 1) // n * c
    cur += (20 * 60 - 60 * h - m) * d
    c *= 0.8
    an = min(an, c * ((cur + n - 1) // n))
else:
    c *= 0.8
    an = c * ((cur + n - 1) // n)
print(an)
