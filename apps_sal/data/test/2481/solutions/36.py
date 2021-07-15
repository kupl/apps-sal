#from statistics import median
#import collections
#aa = collections.Counter(a) # list to list || .most_common(2)で最大の2個とりだせるお a[0][0]
from math import gcd
from itertools import combinations,permutations,accumulate, product # (string,3) 3回
#from collections import deque
from collections import deque,defaultdict,Counter
import decimal
import re
import math
import bisect
import heapq
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
INF = float('inf')
from sys import stdin
readline = stdin.readline
def readInts():
  return list(map(int,readline().split()))
def readTuples():
    return tuple(map(int,readline().split()))
def I():
    return int(readline())
class WarshallFloyd(object):
    def __init__(self):
        self.max_v = 10
        self.min_dist = [readInts() for _ in range(10)]
    def compute(self):
        for k,i,j in product(list(range(self.max_v)), repeat = 3):
            # i -> j と i -> k -> j のうち、長くない方の距離
            self.min_dist[i][j] = min(self.min_dist[i][j], self.min_dist[i][k] + self.min_dist[k][j])
    def solve(self, n):
        if n == 1:
            return 0
        else:
            return self.min_dist[n][1]
h,w = readInts()
w = WarshallFloyd()
w.compute()
ans = 0
A = [readInts() for _ in range(h)]
for a in A:
    for i in a:
        if i == -1:
            continue
        ans += w.solve(i)
print(ans)

