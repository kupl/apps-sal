import math
from fractions import Decimal
from decimal import *
getcontext().prec = 100
x = Decimal(input())


def tows(n):
    ans = Decimal(0)
    while(n > 0):
        ans += Decimal(2**n)
        n -= 1
    return ans


k = True
answer = []
for n in range(100, -1, -1):
    d = tows(n)
    b = (d - 1)
    ans = []
    s = Decimal(Decimal(b**2) + Decimal(8 * x))
    s = s.sqrt()
    h = Decimal(-b / 2)
    ans.append(h + s / 2)
    ans.append(h - s / 2)
    for item in ans:
        if(item < 1 or item % 2 != 1):
            continue
        answer.append(item * (2**(n)))
        k = False
if(k):
    print(-1)
answer.sort()
for item in answer:
    print(int(item))
