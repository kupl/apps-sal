from bisect import bisect_left as bl, bisect_right as br
from collections import defaultdict as dd, Counter
from math import ceil
from math import gcd
import sys
INF = 10**20
MOD = 10**9 + 7
I = lambda: list(map(int, input().split()))


"""
Facts and Data representation
Constructive? Top bottom up down
"""


def find(x):
    ans = []
    for i in range(1, int(x ** 0.5) + 1):
        if x % i:
            continue
        ans.append(i)
        ans.append(x // i)
    return ans


def solve():
    n, = I()
    a = I() * 2
    ans = sum(a) // 2
    mn = INF
    odd = even = 0
    for i in range(n - 1):
        if i % 2:
            odd += a[i]
        else:
            even += a[i]
    mn = min(odd, even)
    back = n - 1
    for i in range(n - 1, 2 * n):
        if i % 2:
            odd += a[i]
            odd -= a[i - back]
        else:
            even += a[i]
            even -= a[i - back]
        mn = min(mn, odd, even)
    print(ans - mn)


solve()
