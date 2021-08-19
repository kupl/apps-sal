from decimal import ROUND_HALF_UP, Decimal
from collections import deque, Counter, defaultdict
from bisect import bisect_left as bileft, bisect_right as biright
from functools import lru_cache
from math import sqrt, ceil
import sys
mod = 10 ** 9 + 7
inf = float('inf')


def input():
    return sys.stdin.readline().strip()


sys.setrecursionlimit(11451419)
(n, m) = list(map(int, input().split()))
A = [int(input()) for i in range(m)]
NG = [0] * (10 ** 5 + 10)
for i in A:
    NG[i] = 1


@lru_cache(maxsize=10 ** 10)
def qwe(x):
    if x == n:
        return 1
    if x > n:
        return 0
    if NG[x + 1] and NG[x + 2]:
        print(0)
        return
    if NG[x + 1]:
        return qwe(x + 2) % mod
    if NG[x + 2]:
        return qwe(x + 1) % mod
    return (qwe(x + 2) + qwe(x + 1)) % mod


print(qwe(0))
