from collections import Counter
import bisect
from itertools import permutations
import sys
import math


def R():
    return map(int, input().split())


def I():
    return int(input())


def S():
    return str(input())


def L():
    return list(R())


(n, m, w) = R()
a = L()
l = 0
r = 10 ** 10
while l < r - 1:
    mid = (l + r) // 2
    b = [0] * n
    fl = True
    cur = 0
    days = 0
    for i in range(n):
        cur += b[i]
        if a[i] + cur < mid:
            delta = mid - a[i] - cur
            days += delta
            cur += delta
            if i + w < n:
                b[i + w] -= delta
        if days > m:
            fl = False
            break
    if fl:
        l = mid
    else:
        r = mid
print(l)
