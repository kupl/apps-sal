import sys
import math
import itertools
import bisect
from copy import copy
from collections import deque, Counter
from decimal import Decimal


def s():
    return input()


def i():
    return int(input())


def S():
    return input().split()


def I():
    return map(int, input().split())


def L():
    return list(input().split())


def l():
    return list(map(int, input().split()))


def lcm(a, b):
    return a * b // math.gcd(a, b)


sys.setrecursionlimit(10 ** 9)
INF = 10 ** 9
mod = 10 ** 9 + 7
(H, W) = I()
N = i()
a = l()
list = []
for i in range(N):
    for j in range(a[i]):
        list.append(i + 1)
ans = [[] for _ in range(H)]
for i in range(H):
    for j in range(W):
        ans[i].append(list.pop(0))
for i in range(H):
    if i % 2 == 1:
        print(*ans[i][::-1])
    else:
        print(*ans[i])
