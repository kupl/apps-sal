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
H,W,M = readInts()

dic1 = Counter()
dic2 = Counter()
s = set()
for i in range(M):
    h,w = [int(x)-1 for x in input().split()]
    dic1[h] += 1
    dic2[w] += 1
    s.add((h,w))
# print(dic)
ans = 0

# 重なっているもので最大値がある時もあれば
# 行、列の交差点でボムなしが一番大きいものがある
for h,w in s:
    ans = max(ans, dic1[h] + dic2[w] - 1)

dic1 = dic1.most_common()
dic2 = dic2.most_common()
max1 = dic1[0][1]
max2 = dic2[0][1]

for k1,v1 in dic1:
    if v1 < max1:
        break # continueする必要がない most_commonで大きい方から集めてるので
    for k2,v2 in dic2:
        if v2 < max2:
            break # 同じく
        if (k1,k2) in s: # 一度計算したもの
            continue
        # 両方とも最大であればok
        ans = max(ans, v1 + v2)
        break
print(ans)

