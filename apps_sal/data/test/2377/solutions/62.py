#from statistics import median
#import collections
#aa = collections.Counter(a) # list to list || .most_common(2)で最大の2個とりだせるお a[0][0]
from fractions import gcd
from itertools import combinations,permutations,accumulate, product # (string,3) 3回
#from collections import deque
from collections import deque,defaultdict,Counter
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
from sys import stdin
readline = stdin.readline
def readInts():
  return list(map(int,readline().split()))
def readTuples():
    return tuple(map(int,readline().split()))
def I():
  return int(readline())
n,h = readInts()
A = [0] * n
B = [0] * n
for i in range(n):
    a,b = readInts()
    A[i] = a
    B[i] = b
A = sorted(A, reverse = True)
B = sorted(B, reverse = True)
MAX = A[0]
ans = 0
for v in B:
    # 投げれるMAXより大きい物はぶん投げろ
    if h <= 0:
        break
    if v > MAX: # 投げろ
        # いつ投げても一緒だねえ
        ans += 1
        h -= v
    else:
        break
if h > 0:
    ans += (h + MAX - 1) // MAX # 振れるやつ限界まで振ってやろう
print(ans)

