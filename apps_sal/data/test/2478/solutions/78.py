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

sys.setrecursionlimit(int(1e6))


def solve():
    n = int(input())
    s = input()

    stack = [-1]
    for e in s:
        if e == '(':
            stack.append(e)
        else:
            if stack[-1] == '(':
                stack.pop()
            else:
                stack.append(e)
    l = stack.count(')')
    r = stack.count('(')
    print(('(' * l + s + ')' * r))


T = 1
for case in range(1, T + 1):
    ans = solve()


"""

dp[num_changes][blue_placed]


abba



"""
