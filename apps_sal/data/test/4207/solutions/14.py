"""input
3
1 2 -1
-6 -12 6
"""
from math import gcd
import sys
from collections import defaultdict as dd
from itertools import permutations as pp
from itertools import combinations as cc
from collections import Counter as ccd
from random import randint as rd
from bisect import bisect_left as bl
import heapq
mod = 10 ** 9 + 7


def ri(flag=0):
    if flag == 0:
        return [int(i) for i in sys.stdin.readline().split()]
    else:
        return int(sys.stdin.readline())


n = ri(1)
a = ri()
b = ri()
k = dd(int)
k[0, 0, 0] = 0
for i in range(n):
    ok = gcd(a[i], b[i])
    f = 0
    if a[i] != 0 and b[i] != 0:
        one = a[i] // ok
        two = b[i] // ok
        f = f ^ (one < 0)
        f = f ^ (two < 0)
        one = abs(one)
        two = abs(two)
        if one != 0:
            k[one, two, f] += 1
    if a[i] != 0 and b[i] == 0:
        pass
    if a[i] == 0 and b[i] == 0:
        k[0, 0, 0] += 1
ans = b.count(0)
for i in k:
    if i == (0, 0, 0):
        ans = max(ans, k[i])
    else:
        ans = max(ans, k[0, 0, 0] + k[i])
print(ans)
