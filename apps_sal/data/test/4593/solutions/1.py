#from statistics import median
#import collections
# aa = collections.Counter(a) # list to list || .most_common(2)で最大の2個とりだせるお a[0][0]
from sys import stdin
from fractions import gcd
from itertools import combinations, permutations, accumulate, product  # (string,3) 3回
#from collections import deque
from collections import deque, defaultdict, Counter
import decimal
import re
import math

#
#
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
import sys
sys.setrecursionlimit(10000000)
mod = 10**9 + 7
#mod = 9982443453
#mod = 998244353
readline = stdin.readline


def readInts():
    return list(map(int, readline().split()))


def readTuples():
    return tuple(map(int, readline().split()))


def I():
    return int(readline())


x = I()
ans = -1
for b in range(1, x + 2):
    for p in range(2, x + 2):
        if b**p > x:
            break
        ans = max(ans, b**p)
print(ans)
