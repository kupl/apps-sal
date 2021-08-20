from bisect import bisect_left as bl
from bisect import bisect_right as br
from heapq import heappush, heappop
import math
from collections import *
from functools import reduce, cmp_to_key
import sys
input = sys.stdin.readline
M = mod = 998244353


def factors(n):
    return sorted(set(reduce(list.__add__, ([i, n // i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0))))


def inv_mod(n):
    return pow(n, mod - 2, mod)


def li():
    return [int(i) for i in input().rstrip('\n').split()]


def st():
    return input().rstrip('\n')


def val():
    return int(input().rstrip('\n'))


def li2():
    return [i for i in input().rstrip('\n')]


def li3():
    return [int(i) for i in input().rstrip('\n')]


for _ in range(val()):
    (x, y) = li()
    (c1, c2, c3, c4, c5, c6) = li()
    for i in range(30):
        c1 = min(c1, c2 + c6)
        c6 = min(c6, c1 + c5)
        c5 = min(c5, c6 + c4)
        c4 = min(c4, c5 + c3)
        c2 = min(c2, c1 + c3)
        c3 = min(c3, c2 + c4)
    temp = min(abs(x), abs(y))
    if x >= 0 and y >= 0:
        x -= temp
        y -= temp
        ans = temp * c1 + x * c6 + y * c2
    elif x <= 0 and y >= 0:
        x = abs(x)
        ans = x * c3 + y * c2
    elif x >= 0 and y <= 0:
        y = abs(y)
        ans = x * c6 + y * c5
    else:
        x += temp
        y += temp
        x = abs(x)
        y = abs(y)
        ans = temp * c4 + x * c3 + y * c5
    print(ans)
