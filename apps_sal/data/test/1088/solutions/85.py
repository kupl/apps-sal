import math
from math import gcd,pi,sqrt
INF = float("inf")
MOD = 10**9 + 7
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
import itertools
import bisect
import re
from collections import Counter,deque,defaultdict
def iinput(): return int(input())
def imap(): return map(int, input().split())
def ilist(): return list(imap())
def irow(N): return [iinput() for i in range(N)]
def sinput(): return input().rstrip()
def smap(): return sinput().split()
def slist(): return list(smap())
def srow(N): return [sinput() for i in range(N)]

def main():
    MOD = 998244353
    class UnionFind:
        def __init__(self, n):
            self.par = [i for i in range(n+1)]
            self.rank = [0] * (n+1)
            self.size = [1] * (n+1) # 親に集約される
    
        # 検索
        def find(self, x):
            if self.par[x] == x:
                return x
            else:
                self.par[x] = self.find(self.par[x])
                return self.par[x]
    
        # 併合
        def union(self, x, y):
            x = self.find(x)
            y = self.find(y)
    
            if x == y:
                return
    
            if self.rank[x] < self.rank[y]:
                self.par[x] = y
                self.size[y] += self.size[x]
                self.size[x] = 0
            else:
                self.par[y] = x
                self.size[x] += self.size[y]
                self.size[y] = 0
                if self.rank[x] == self.rank[y]:
                    self.rank[x] += 1
    
        # 同じ集合に属するか判定
        def same(self, x, y):
            return self.find(x) == self.find(y)
    
        # すべての頂点に対して親を検索する
        def all_find(self):
            for n in range(len(self.par)):
                self.find(n)
    N,K = imap()
    import numpy as np
    A = np.array([ilist() for i in range(N)])
    uf_i = UnionFind(N)
    uf_r = UnionFind(N)

    for i in range(N-1):
        for j in range(i+1,N):
            if np.all(A[i] + A[j] <= K):
                uf_i.union(i+1,j+1)
            if np.all(A[:,i] + A[:,j] <= K):
                uf_r.union(i+1, j+1)
    uf_i.all_find()
    uf_r.all_find()
    
    ans = 1
    for i in uf_i.size:
        if i in [0,1]:
            continue
        ans *= math.factorial(i)
    for j in uf_r.size:
        if j in [0,1]:
            continue
        ans *= math.factorial(j)
    print(ans%MOD)



def __starting_point():
    main()
__starting_point()
