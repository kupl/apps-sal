from bisect import bisect_right as br
from bisect import bisect_left as bl
from math import *


def isprime(n):
    n = abs(int(n))
    if n < 2:
        return False
    if n == 2:
        return True
    if not n & 1:
        return False
    for x in range(3, int(n ** 0.5) + 1, 2):
        if n % x == 0:
            return False
    return True


def mhd(a, b, x, y):
    return abs(a - x) + abs(b - y)


ta = []
pa = []
d = {}
(n, m) = map(int, input().split())
a = list(map(int, input().split()))
t = list(map(int, input().split()))
for i in range(n + m):
    if t[i] == 1:
        ta.append(a[i])
        d[a[i]] = 0
    else:
        pa.append(a[i])
if m == 1:
    print(n)
else:
    ta.sort()
    for i in pa:
        li = bl(ta, i)
        if li == 0:
            d[ta[li]] += 1
        elif li == m:
            d[ta[li - 1]] += 1
        else:
            x = abs(ta[li - 1] - i)
            y = abs(ta[li] - i)
            if x <= y:
                d[ta[li - 1]] += 1
            else:
                d[ta[li]] += 1
    for i in range(n + m):
        if t[i] == 1:
            print(d[a[i]], end=' ')
