from math import *
from bisect import *
a1 = int(input())
a2 = int(input())
k1 = int(input())
k2 = int(input())
n = int(input())
(maxx, minn) = (0, 1230120)
if k1 < k2:
    if n // k1 > a1:
        maxx += a1
        maxx += min((n - k1 * a1) // k2, a2)
    else:
        maxx += n // k1
elif n // k2 > a2:
    maxx += a2
    maxx += min((n - k2 * a2) // k1, a1)
else:
    maxx += n // k2
n -= (k1 - 1) * a1 + (k2 - 1) * a2
if n <= 0:
    minn = 0
else:
    minn = n
print(minn, maxx)
