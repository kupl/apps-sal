from math import ceil,floor,factorial,gcd,sqrt,log2,cos,sin,tan,acos,asin,atan,degrees,radians,pi,inf,comb
from itertools import accumulate,groupby,permutations,combinations,product,combinations_with_replacement
from collections import deque,defaultdict,Counter
from bisect import bisect_left,bisect_right
from operator import itemgetter
from heapq import heapify,heappop,heappush
from queue import Queue,LifoQueue,PriorityQueue
from copy import deepcopy
from time import time
from functools import reduce
import string
import sys
sys.setrecursionlimit(10 ** 7)
def input() : return sys.stdin.readline().strip()
def INT()   : return int(input())
def MAP()   : return map(int,input().split())
def LIST()  : return list(MAP())

n = INT()
f = []
for i in range(n):
    f.append(LIST())
p = []
for i in range(n):
    p.append(LIST())

ans = -inf
for x in product([0, 1], repeat=10):
    if sum(x) != 0:
        tmp = 0
        for j in range(n):
            count = 0
            for k in range(10):
                count += f[j][k]*x[k]
            tmp += p[j][count]
        ans = max(ans, tmp)
print(ans)
