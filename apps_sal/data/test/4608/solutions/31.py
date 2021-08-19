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


sys.setrecursionlimit(10 ** 6)
mod = 10 ** 9 + 7
cnt = 0
ans = 0
inf = float('inf')
al = 'abcdefghijklmnopqrstuvwxyz'
AL = al.upper()
N = k()
A = []
for i in range(N):
    a = k()
    A.append(a)
aaa = 0
ans = A[0]
count = 1
for i in range(N):
    if ans == 2:
        aaa = 1
        break
    else:
        ans = A[ans - 1]
        count += 1
if aaa == 1:
    print(count)
else:
    print(-1)
