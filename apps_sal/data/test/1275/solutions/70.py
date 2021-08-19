#
#
#
# 笑え、君が好きなように。
#                         笑いは世界を救う。
#                                           あなたが笑ってくれるなら。
#
#from statistics import median
#import collections
# aa = collections.Counter(a) # list to list || .most_common(2)で最大の2個とりだせるお a[0][0]
from sys import stdin
from math import gcd
from itertools import combinations, permutations, accumulate, product, combinations_with_replacement  # (string,3) 3回
from collections import deque, defaultdict, Counter
import decimal
import re
import math
import bisect
import heapq
#
# set型だと、 | と & が使えるよ
#
# pythonで無理なときは、pypyでやると正解するかも！！
#
#
# my_round_int = lambda x:np.round((x*2 + 1)//2)
# 四捨五入g
#
# インデックス系
# int min_y = max(0, i - 2), max_y = min(h - 1, i + 2);
# int min_x = max(0, j - 2), max_x = min(w - 1, j + 2);
#
#
# 整数か判定する
# nanka.is_integer()
# ref https://atcoder.jp/contests/abc133/tasks/abc133_b
import sys
sys.setrecursionlimit(10000000)
mod = 10**9 + 7
# mod = 9982443453
# mod = 998244353
INF = float('inf')
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
readline = stdin.readline


def readInts():
    return list(map(int, readline().split()))


def readTuples():
    return tuple(map(int, readline().split()))


def I():
    return int(readline())


def f(n):
    return int(math.ceil(n - 0.5))


#from statistics import median
#import collections
# aa = collections.Counter(a) # list to list || .most_common(2)で最大の2個とりだせるお a[0][0]
#from collections import deque
#
# set型だと、 | と & が使えるよ
#
# pythonで無理なときは、pypyでやると正解するかも！！
#
#
# my_round_int = lambda x:np.round((x*2 + 1)//2)
# 四捨五入g
#
# インデックス系
# int min_y = max(0, i - 2), max_y = min(h - 1, i + 2);
# int min_x = max(0, j - 2), max_x = min(w - 1, j + 2);
#
#
# 整数か判定する
# nanka.is_integer()
# ref https://atcoder.jp/contests/abc133/tasks/abc133_b
sys.setrecursionlimit(10000000)
mod = 10**9 + 7
# mod = 9982443453
# mod = 998244353
INF = float('inf')
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
readline = stdin.readline


def readInts():
    return list(map(int, readline().split()))


def readTuples():
    return tuple(map(int, readline().split()))


def I():
    return int(readline())


def f(n):
    return int(math.ceil(n - 0.5))


N, K = readInts()


def calc(n):
    if n <= 0:
        return 0
    elif n > 2 * N:
        return 0
    else:
        return min(2 * N - n + 1, n - 1)


ans = 0
for i in range(1, 2 * N + 1):
    ans += calc(i) * calc(i - K)
print(ans)
