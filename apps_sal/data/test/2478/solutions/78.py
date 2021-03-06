from functools import lru_cache, reduce
from bisect import bisect_left, bisect_right
import random
import operator
import string
import sys
from collections import deque, defaultdict, namedtuple
import heapq
from math import sqrt, factorial, gcd, ceil, atan, pi


def input():
    return sys.stdin.readline()[:-1]


MOD = int(1000000000.0) + 7
INF = float('inf')
sys.setrecursionlimit(int(1000000.0))


def solve():
    n = int(input())
    s = input()
    stack = [-1]
    for e in s:
        if e == '(':
            stack.append(e)
        elif stack[-1] == '(':
            stack.pop()
        else:
            stack.append(e)
    l = stack.count(')')
    r = stack.count('(')
    print('(' * l + s + ')' * r)


T = 1
for case in range(1, T + 1):
    ans = solve()
'\n\ndp[num_changes][blue_placed]\n\n\nabba\n\n\n\n'
