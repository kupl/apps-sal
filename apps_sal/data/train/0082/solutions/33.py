# -*- coding: utf-8 -*-
import sys
from collections import deque, defaultdict
from math import sqrt, factorial, gcd, ceil, atan, pi
def input(): return sys.stdin.readline()[:-1] # warning not \n
# def input(): return sys.stdin.buffer.readline().strip() # warning bytes
# def input(): return sys.stdin.buffer.readline().decode('utf-8')
import string
# string.ascii_lowercase
from bisect import bisect_left, bisect_right
from functools import lru_cache
MOD = int(1e9)+7
INF = float('inf')


def solve():
    n = int(input())
    p = [int(x) for x in input().split()]
    p.reverse()
    print(*p)
        

    
t = 1
t = int(input())
for case in range(1,t+1):
    ans = solve()


"""


"""

