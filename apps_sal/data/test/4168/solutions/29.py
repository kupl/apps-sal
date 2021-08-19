# -*- coding: utf-8 -*-
import sys
from collections import deque, defaultdict
from math import sqrt, factorial, gcd, ceil, atan, pi
# def input(): return sys.stdin.readline()[:-1] # warning not \n
# def input(): return sys.stdin.buffer.readline().strip() # warning bytes
# def input(): return sys.stdin.buffer.readline().decode('utf-8')
import string
# string.ascii_lowercase
from bisect import bisect_left
MOD = int(1e9) + 7
INF = float('inf')


def solve():
    # n, m = [int(x) for x in input().split()]
    # n, m = [int(x) for x in input().split()]
    n = -int(input())
    if n == 0:
        print((0))
        return
    ans = []
    while n != 0:
        n, m = divmod(n, -2)
        ans.append(-m)

    ans.reverse()
    print((''.join([str(x) for x in ans])))


t = 1
# t = int(input())
for case in range(1, t + 1):
    ans = solve()


"""

"""
