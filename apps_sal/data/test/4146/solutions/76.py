import sys
import bisect
import math
import itertools
import string
import queue
import copy
from collections import Counter, defaultdict, deque
from itertools import permutations, combinations
from heapq import heappop, heappush
from fractions import gcd
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)
mod = 10 ** 9 + 7


def inp():
    return int(input())


def inpm():
    return list(map(int, input().split()))


def inpl():
    return list(map(int, input().split()))


def inpls():
    return list(input().split())


def inplm(n):
    return list((int(input()) for _ in range(n)))


def inplL(n):
    return [list(input()) for _ in range(n)]


def inplT(n):
    return [tuple(input()) for _ in range(n)]


def inpll(n):
    return [list(map(int, input().split())) for _ in range(n)]


def inplls(n):
    return sorted([list(map(int, input().split())) for _ in range(n)])


n = inp()
a = inpl()
cnt_even = defaultdict(int)
cnt_odd = defaultdict(int)
for i in range(0, n, 2):
    cnt_even[a[i]] += 1
for i in range(1, n, 2):
    cnt_odd[a[i]] += 1
cnt_even = list(reversed(sorted(list(cnt_even.items()), key=lambda x: x[1])))
cnt_odd = list(reversed(sorted(list(cnt_odd.items()), key=lambda x: x[1])))
flg = False
for i in range(min(2, len(cnt_even), len(cnt_odd))):
    (a, b) = (cnt_even[i], cnt_odd[i])
    if a[0] != b[0]:
        if flg == False:
            n -= a[1] + b[1]
        else:
            n -= max(a[1], b[1])
        break
    else:
        n -= a[1]
        flg = True
print(n)
