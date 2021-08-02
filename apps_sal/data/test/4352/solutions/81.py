import sys
import math
from functools import lru_cache
from itertools import accumulate
sys.setrecursionlimit(10**9)
MOD = 10**9 + 7


def input():
    return sys.stdin.readline()[:-1]


def mi():
    return map(int, input().split())


def ii():
    return int(input())


def i2(n):
    tmp = [list(mi()) for i in range(n)]
    return [list(i) for i in zip(*tmp)]


A, B = mi()

if A == B:
    print('Draw')
elif A == 1:
    print('Alice')
elif B == 1:
    print('Bob')
else:
    if A > B:
        print('Alice')
    else:
        print('Bob')
