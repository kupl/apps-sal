# region header
import sys, bisect, math, itertools, heapq, collections
from operator import itemgetter
# a.sort(key=itemgetter(i)) # i番目要素でsort
from functools import lru_cache
import copy
# @lru_cache(maxsize=None)
# sys.setrecursionlimit(10**8)
input = sys.stdin.readline
INF = float('inf')
mod = 10**9 + 7
eps = 10**-7
# endregion
# region input function


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

# endregion


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

