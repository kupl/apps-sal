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

class WeightedUnionfind():
    def __init__(self,n):
        self.par =[i for i in range(n+1)]
        self.rank =[0]*(n+1)
        self.weight =[0]*(n+1)

    def find(self,x):
        if self.par[x]==x:
            return x

        else:
            y =self.find(self.par[x])
            self.weight[x]+=self.weight[self.par[x]]
            self.par[x]=y
            return y

    def union(self,x,y,w):
        rx=self.find(x)
        ry=self.find(y)
        if self.rank[rx]<self.rank[ry]:
            self.par[rx]=ry
            self.weight[rx]=w-self.weight[x]+self.weight[y]
        else:
            self.par[ry]=rx
            self.weight[ry]=-w-self.weight[y]+self.weight[x]
            if self.rank[rx]==self.rank[ry]:
                self.rank[rx]+=1
    def same(self,x,y):
        return self.find(x)==self.find(y)

    def diff(self,x,y):
        return self.weight[x]-self.weight[y]

n,m=MI()
wuf=WeightedUnionfind(n)
for i in range(m):
    l,r,d=MI()
    #print(l,r,d,end=" ")
    #print(wuf.same(l,r))
    if wuf.same(l,r):
        #print(wuf.diff(l,r))
        if wuf.diff(l,r)!=d:
            print("No")
            return
    else:
        wuf.union(l,r,d)
print("Yes")



    
    



    


        


    
    


    

    
            
        
        
    
    
    
    

    
    


    
    

        
        
    



