from math import ceil,floor,factorial,gcd,sqrt,log2,cos,sin,tan,acos,asin,atan,degrees,radians,pi,inf
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
def MAP1()  : return map(lambda x:int(x)-1,input().split())
def LIST()  : return list(MAP())
def LIST1() : return list(MAP1())

def solve():
    N = INT()
    a = LIST()
    l = [0]*N
    r = [0]*N
    l[0] = a[0]
    r[N-1] = a[N-1]

    for i in range(1, N):
        l[i] = gcd(l[i-1], a[i])
    for i in range(N-2, -1, -1):
        r[i] = gcd(r[i+1], a[i])

    ans = max(r[1], l[N-2])
    for i in range(1, N-1):
        ans = max(ans, gcd(l[i-1], r[i+1]))
    print(ans)
    
def __starting_point():
    solve()
__starting_point()
