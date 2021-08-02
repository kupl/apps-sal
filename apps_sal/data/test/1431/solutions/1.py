# -*- coding: utf-8 -*-
from functools import lru_cache
from bisect import bisect_left, bisect_right
import string
import sys
from collections import deque, defaultdict
from math import sqrt, factorial, gcd, ceil, atan, pi
def input(): return sys.stdin.readline()[:-1]  # warning not \n


# def input(): return sys.stdin.buffer.readline().strip() # warning bytes
# def input(): return sys.stdin.buffer.readline().decode('utf-8')
# string.ascii_lowercase
MOD = int(1e9) + 7
INF = float('inf')


def solve():
    n = int(input())
    a = [int(x) for x in input().split()]
    xd = [0] * n
    ans = []
    for i in range(n - 1, -1, -1):
        cnt = 0
        for j in range(i, n, i + 1):
            cnt += xd[j]
        cnt %= 2
        if cnt != a[i]:
            ans.append(i + 1)
            xd[i] = 1
    ans.reverse()
    print((len(ans)))
    if ans:
        print((*ans))


t = 1
# t = int(input())
for case in range(1, t + 1):
    ans = solve()


"""


"""
