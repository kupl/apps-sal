import sys
import bisect
import math
import itertools
import heapq
import collections
from operator import itemgetter
from functools import lru_cache
import copy
input = sys.stdin.readline
INF = float('inf')
mod = 10**9 + 7
eps = 10**-7


def inp():
    '''
    一つの整数
    '''
    return int(input())


def inpl():
    '''
    一行に複数の整数
    '''
    return list(map(int, input().split()))


def str_inp():
    '''
    文字列をリストとして読み込む
    '''
    return list(input()[:-1])


n, k = inpl()
a = inpl()

l = 0
r = 10**9
while l + 1 < r:
    x = (l + r) // 2
    cnt = 0
    for i in range(n):
        cnt += math.ceil(a[i] / x) - 1
        if cnt > k:
            break
    if cnt <= k:
        r = x
    else:
        l = x
print(r)
