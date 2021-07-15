from math import ceil,floor,factorial,gcd,sqrt,log2,cos,sin,tan,acos,asin,atan,degrees,radians,pi,inf,comb
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

n = INT()
k = INT()

@lru_cache(None)
def F(n, k):
    # n以下で0でないものがちょうどk個ある数字の個数
    if n < 10:
        if k == 0:
            return 1
        if k == 1:
            return n
        return 0
    q, r = divmod(n, 10)
    ret = 0
    if k >= 1:
        # 1の位が0
        ret += F(q, k-1) * r
        ret += F(q-1, k-1) * (9-r)
    ret += F(q, k)
    return ret

print(F(n, k))
