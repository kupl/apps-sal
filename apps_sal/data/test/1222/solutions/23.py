from functools import lru_cache, reduce
from bisect import bisect_left, bisect_right
import random
import operator
import string
import sys
from collections import deque, defaultdict, namedtuple
import heapq
from math import sqrt, factorial, gcd, ceil, atan, pi
def input(): return sys.stdin.readline()[:-1]


MOD = int(1e9) + 7
INF = float('inf')


def print_lines(data):
    sys.stdout.write('\n'.join((str(x) for x in data)))


def solve():
    n = int(input())
    q = deque([x for x in range(1, 10)])
    cur = 0
    while n:
        cur = q.popleft()

        last = cur % 10
        if last == 0:
            q.append(cur * 10)
            q.append(cur * 10 + 1)
        elif last == 9:
            q.append(cur * 10 + last - 1)
            q.append(cur * 10 + last)
        else:
            q.append(cur * 10 + last - 1)
            q.append(cur * 10 + last)
            q.append(cur * 10 + last + 1)

        n -= 1
    print(cur)


T = 1
for case in range(1, T + 1):
    ans = solve()


"""

dp[num_changes][blue_placed]


abba

12123456789


"""
