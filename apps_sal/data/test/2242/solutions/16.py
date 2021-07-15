from math import ceil,floor,factorial,gcd,sqrt,log2,cos,sin,tan,acos,asin,atan,degrees,radians,pi,inf
from itertools import accumulate,groupby,permutations,combinations,product,combinations_with_replacement
from collections import deque,defaultdict,Counter
from bisect import bisect_left,bisect_right
from operator import itemgetter
from heapq import heapify,heappop,heappush
from queue import Queue,LifoQueue,PriorityQueue
from copy import deepcopy
from time import time
from functools import reduce, lru_cache
import string
import sys
sys.setrecursionlimit(10 ** 7)
def input() : return sys.stdin.readline().strip()
def INT()   : return int(input())
def MAP()   : return map(int,input().split())
def MAP1()  : return map(lambda x:int(x)-1,input().split())
def LIST()  : return list(MAP())
def LIST1() : return list(MAP1())

s = input()

@lru_cache(None)
def F(s, k):
    # sの左からk文字目以降を整数と見なしたとき、
    # 2019で割った余りを返す
    if k == len(s)-1:
        return int(s[k])
    ret = F(s, k+1) + int(s[k])*pow(10, len(s)-1-k, 2019)
    ret %= 2019
    return ret

a = [0]*2020
for i in range(len(s)):
    a[F(s, i)] += 1

ans = a[0]
for i in range(2020):
    ans += a[i] * (a[i]-1) // 2

print(ans)
