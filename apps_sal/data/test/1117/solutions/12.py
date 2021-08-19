import math as ma
from decimal import Decimal as dec


def li():
    return list(map(int, input().split()))


def num():
    return list(map(int, input().split()))


def nu():
    return int(input())


n = nu()
a = 0
b = 0
flag = True
for i in range(n):
    (w, h) = num()
    if i == 0:
        a = max(h, w)
        b = min(h, w)
    elif max(h, w) <= a:
        a = max(h, w)
        b = min(h, w)
    elif min(h, w) <= a:
        b = max(h, w)
        a = min(h, w)
    else:
        flag = False
if flag:
    print('YES')
else:
    print('NO')
