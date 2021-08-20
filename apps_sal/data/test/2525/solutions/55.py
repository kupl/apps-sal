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
    return list(map(int, input().split()))


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
al = 'abcdefghijklmnopqrstuvwxyz'
AL = al.upper()
s = deque(X())
n = k()
normal = 0
for i in range(n):
    a = input().split()
    if int(a[0]) == 1:
        normal ^= 1
    else:
        k = int(a[1]) - 1
        k ^= normal
        if k == 1:
            s.append(a[2])
        else:
            s.appendleft(a[2])
print(''.join(s) if normal == 0 else ''.join(list(s)[::-1]))
