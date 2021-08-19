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
x = int(input())
if x % 11 == 0:
    print(x // 11 * 2)
else:
    print(x // 11 * 2 + x % 11 // 7 + 1)
