# python 3.4.3
import sys
input = sys.stdin.readline
import numpy as np

# -------------------------------------------------------------
# function
# -------------------------------------------------------------
class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n+1)]
        self.rank = [0]*(n+1)
    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]
    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1
    def check(self, x, y):
        return self.find(x) == self.find(y)

# -------------------------------------------------------------
# main
# -------------------------------------------------------------
N,K,L = map(int,input().split())
PQ = [tuple(map(int,input().split())) for _ in range(K)]
RS = [tuple(map(int,input().split())) for _ in range(L)]

# 道路
A = UnionFind(N)
for p,q in PQ:
    A.unite(p-1,q-1)
 
# 鉄道
B = UnionFind(N)
for r,s in RS:
    B.unite(r-1,s-1)

# 集計
from collections import defaultdict
dic = defaultdict(int)
for i in range(N):
    dic[A.find(i), B.find(i)] += 1
 
Ans = list(dic[A.find(i), B.find(i)] for i in range(N))
print(" ".join(map(str,Ans)))
