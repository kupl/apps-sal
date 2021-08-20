import sys
from collections import deque, defaultdict
from math import sqrt, factorial, gcd, ceil, atan, pi
import string
from bisect import bisect_left
MOD = int(1000000000.0) + 7
INF = float('inf')


def solve():
    n = -int(input())
    if n == 0:
        print(0)
        return
    ans = []
    while n != 0:
        (n, m) = divmod(n, -2)
        ans.append(-m)
    ans.reverse()
    print(''.join([str(x) for x in ans]))


t = 1
for case in range(1, t + 1):
    ans = solve()
'\n\n'
