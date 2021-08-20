import re
import sys
import math
import itertools
import bisect
from copy import copy
from collections import deque, Counter
from decimal import Decimal
import functools


def v():
    return input()


def k():
    return int(input())


def S():
    return input().split()


def I():
    return map(int, input().split())


def X():
    return list(input())


def L():
    return list(input().split())


def l():
    return list(map(int, input().split()))


def lcm(a, b):
    return a * b // math.gcd(a, b)


sys.setrecursionlimit(10 ** 9)
mod = 10 ** 9 + 7
cnt = 0
ans = 0
inf = float('inf')
n = k()
h = l()
for i in range(1, n):
    if h[i - 1] - h[i] > 0:
        ans += h[i - 1] - h[i]
print(ans + h[-1])
'\nn = k()\ns = v()\n\ndef check(n):\n    if \n\n#コマンドの種類\ncomand = ["A","B","X","Y"]\np = list(itertools.permutations(comand,2))\nfor i in range(len(p)):\n    p[i] = "".join(p[i])\n\nfor i in \n'
