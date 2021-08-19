#from statistics import median
#import collections
# aa = collections.Counter(a) # list to list || .most_common(2)で最大の2個とりだせるお a[0][0]
from fractions import gcd
from itertools import combinations, permutations, accumulate, product  # (string,3) 3回
#from collections import deque
from collections import deque, defaultdict, Counter
import decimal
import re
#import bisect
#
#    d = m - k[i] - k[j]
#    if kk[bisect.bisect_right(kk,d) - 1] == d:
#
#
#
# pythonで無理なときは、pypyでやると正解するかも！！
#
#
# my_round_int = lambda x:np.round((x*2 + 1)//2)
# 四捨五入g
import sys
sys.setrecursionlimit(10000000)
mod = 10**9 + 7
#mod = 9982443453


def readInts():
    return list(map(int, input().split()))


def I():
    return int(input())


s = input()
l = len(s)
ans = [1] * l
for i in range(l):
    if s[i] == 'R' and s[i + 1] == 'R':
        ans[i + 2] += ans[i]
        ans[i] = 0
for i in range(l - 1, 0, -1):
    if s[i - 1] == 'L' and s[i] == 'L':
        ans[i - 2] += ans[i]
        ans[i] = 0
print((*ans))
