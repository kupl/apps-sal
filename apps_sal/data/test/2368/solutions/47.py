def N():
    return int(input())
def L():
    return list(map(int,input().split()))
def NL(n):
    return [list(map(int,input().split())) for i in range(n)]
mod = pow(10,9)+7
#import numpy as np
import sys
sys.setrecursionlimit(2147483647)
import math
from itertools import accumulate
from itertools import permutations
from collections import Counter
from collections import deque
from collections import defaultdict
import bisect
import heapq
inf = float('inf')
dic = defaultdict(lambda:0)

class UnionFind():
    par = []
    rank = []
    def __init__(self,n):
        for i in range(n):
            self.par.append(i)
            self.rank.append(0)
    def root(self,x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.root(self.par[x])
            return self.par[x]
 
    def same(self,x,y):
        if self.root(x) == self.root(y):
            return True
        else:
            return False
 
    def unite(self,x,y):
        x = self.root(x)
        y = self.root(y)
        if x==y:
            return
        if self.rank[x] > self.rank[y]:
            self.par[y] = x
        else:
            self.par[x] = y
            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1

    def comp(self):#rootまでの距離圧縮
        for i in range(len(self.par)):
            self.root(i)

n,m = L()
a = L()
b = L()
cd = NL(m)
uf = UnionFind(n)
for c,d in cd:
    uf.unite(c-1,d-1)
uf.comp()

va = defaultdict(int)
vb = defaultdict(int)

for i in range(n):
    va[uf.par[i]] += a[i]
    vb[uf.par[i]] += b[i]

for i in range(n):
    if va[i] != vb[i]:
        print('No')
        break
else:
    print('Yes')
