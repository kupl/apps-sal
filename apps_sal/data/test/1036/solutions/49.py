import bisect
import copy
import heapq
import math
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
(n, k) = map(int, input().split())
s = list(input())


def check(a, b):
    if a == b:
        return 0
    elif a == 'R':
        if b == 'P':
            return 1
        else:
            return 0
    elif a == 'P':
        if b == 'S':
            return 1
        else:
            return 0
    elif b == 'R':
        return 1
    else:
        return 0


lst = s
for i in range(k):
    sanka = 2 ** (k - i)
    tmp = []
    if len(lst) % 2:
        lst = lst + lst
    m = min(len(lst), sanka)
    for j in range(m // 2):
        kk = check(lst[2 * j], lst[2 * j + 1])
        tmp.append(lst[2 * j + kk])
    lst = tmp[:]
print(lst[0])
