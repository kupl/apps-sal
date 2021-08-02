import math as ma
import sys
from decimal import Decimal as dec
from itertools import permutations


def li():
    return list(map(int, input().split()))


def num():
    return map(int, input().split())


def nu():
    return int(input())


n, m = num()
a = li()
ind = -1
z = 0
ll = sorted(a)
mx = ll[n - 1] - 1
cc = 0
for i in range(n - 2, -1, -1):
    if (ll[i] == 0):
        continue
    if(mx == 0):
        cc += ll[i] - 1
        continue

    if(ll[i] >= mx):
        cc += 1
        mx -= 1
        cc += ll[i] - 1
        ll[i] = 1
    else:
        mx = ll[i]
        cc += 1
        mx -= 1
        cc += ll[i] - 1
        ll[i] = 1

print(cc)
