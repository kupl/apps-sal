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
ans = 1
inf = float('inf')
al = 'abcdefghijklmnopqrstuvwxyz'
S = v()
a = len(S)
if a % 2 == 0:
    ra = a // 2
else:
    ra = a // 2
for i in range(ra):
    if S[i] != S[-(i + 1)]:
        cnt += 1
print(cnt)
