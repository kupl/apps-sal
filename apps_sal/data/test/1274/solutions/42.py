#import math
#import itertools
#import numpy as np
import heapq
#from collections import deque
# sys.setrecursionlimit(10 ** 6)
#mod = 10 ** 9 + 7
#INF = 10 ** 9
#PI = 3.14159265358979323846

INT = lambda: int(input())
INTM = lambda: map(int,input().split())
STRM = lambda: map(str,input().split())
STR = lambda: str(input())
LIST = lambda: list(map(int,input().split()))
LISTS = lambda: list(map(str,input().split()))

def do():
    n,m=INTM()
    ptj=[[] for i in range(10**5)]
    ans=0
    for i in range(n):
        a,b=INTM()
        a-=1
        b*=(-1)
        ptj[a].append(b)
    h=[]
    for i in range(m):
        for p in ptj[i]:
            heapq.heappush(h,p)
        if len(h)!=0:
            ans+=heapq.heappop(h)
        #print(ans)
    print(0-ans)
    

def __starting_point():
    do()
__starting_point()
