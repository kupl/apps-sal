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
s1 = input()
s2 = input()

ans = 3
i = 1
while i < n:
    if i == 1 or s1[i-1] != s1[i-2]:
        if i == n-1 or s1[i] != s1[i+1]:
            ans = ans * 2 % ( 10**9 + 7 )
            i += 1
        else:
            ans = ans * 2 % ( 10**9 + 7 )
            i += 2
    else:
        if i == n-1 or s1[i] != s1[i+1]:
            ans = ans * 1 % ( 10**9 + 7 )
            i += 1
        else:
            ans = ans * 3 % ( 10**9 + 7 )
            i += 2
print(ans)
