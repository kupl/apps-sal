import bisect
import copy
import heapq
import math
from math import inf
import sys
from collections import *
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product


def input():
    return sys.stdin.readline()[:-1]


def ruiseki(lst):
    return [0] + list(accumulate(lst))


def celi(a, b):
    return -(-a // b)


sys.setrecursionlimit(5000000)
mod = pow(10, 9) + 7
al = [chr(ord('a') + i) for i in range(26)]
direction = [[1, 0], [0, 1], [-1, 0], [0, -1]]

n = int(input())
a = [int(input()) for i in range(n)]

now = n
lst = [-1] * n

for i in range(n):
    tmp = bisect.bisect_left(lst, a[i])
    if tmp == now:
        lst[tmp - 1] = a[i]
        now -= 1
    else:
        lst[tmp - 1] = a[i]
# print(lst)
print(n - now)
