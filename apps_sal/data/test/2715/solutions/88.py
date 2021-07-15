#float型を許すな
#numpyはpythonで
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
from collections import Counter, deque
from collections import defaultdict
from itertools import combinations, permutations, accumulate, groupby, product
from bisect import bisect_left,bisect_right
from heapq import heapify, heappop, heappush
from math import floor, ceil,pi,factorial
from operator import itemgetter
import copy
def I(): return int(input())
def MI(): return list(map(int, input().split()))
def LI(): return list(map(int, input().split()))
def LI2(): return [int(input()) for i in range(n)]
def MXI(): return [[LI()]for i in range(n)]
def SI(): return input().rstrip()
def printns(x): print(('\n'.join(x)))
def printni(x): print(('\n'.join(list(map(str,x)))))
inf = 10**17
mod = 10**9 + 7

n=I()
lis=[50 for i in range(50)]
lists=[]
for i in range(50):
    mx=-inf
    for j in range(50):
        if lis[j]>=mx:
            mx=lis[j]
            ind=j
    for j in range(50):
        lis[j]+=1
    lis[ind]-=51
    lists.append(copy.deepcopy(lis))
    #print(lis)
#print(lists)
#print(lists[0])
u=n%50
x=n//50
base=lists[50-u-1]
for i in range(50):
    base[i]+=x
print((50))
print((*base))




        

    
    
    
    
    

    

