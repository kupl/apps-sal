from functools import reduce
from decimal import *
import math
import itertools


class pair(list):
    def __init__(self, a, b):
        list.__init__(self, (a, b))

    def __add__(self, q): return pair(self[0] + q[0], self[1] + q[1])
    def __sub__(self, q): return pair(self[0] - q[0], self[1] - q[1])
    def __mul__(self, k): return pair(k * self[0], k * self[1])
    def __neg__(self): return pair(-self[0], -self[1])


setcontext(ExtendedContext)
getcontext().prec = 100
a, b, c = pair(1, 2), pair(-2, 0), pair(-1, 2)
n = int(input())
k = int(((Decimal(3 + 4 * n) / Decimal(3)).sqrt() - Decimal(1)) // 2)
n1 = n - 3 * k * (k + 1)
x, y = n1 // (k + 1), n1 % (k + 1)
L = [c, b, -a, -c, -b, a]
M = [pair(0, 0)] + list(itertools.accumulate(L))
if n1 == 0:
    ans = pair(2, 0) * k
else:
    ans = pair(2, 0) * (k + 1) + M[x] * (k + 1) + L[x] * y
print(ans[0], ans[1])
