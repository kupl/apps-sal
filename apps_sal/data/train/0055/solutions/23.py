from bisect import bisect_left as bl, bisect_right as br
from collections import defaultdict as dd, Counter
from math import ceil
from math import gcd
import sys
INF = 10**20
MOD = 10**9 + 7
def I(): return list(map(int, input().split()))


"""
Facts and Data representation
Constructive? Top bottom up down
"""


def solve():
    n, = I()
    if n % 2:
        print(1 + n // 2)
    else:
        print(n // 2)


t, = I()
while t:
    t -= 1
    solve()
