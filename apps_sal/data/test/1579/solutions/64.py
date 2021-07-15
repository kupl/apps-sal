from sys import stdin
import sys
import numpy as np
import collections
from functools import cmp_to_key
import heapq
sys.setrecursionlimit(100000)

##  input functions for me
def rsa(sep = ''):
    if sep == '' :
        return input().split() 
    else: return input().split(sep)
def rip(sep = ''):
    if sep == '' :
        return list(map(int, input().split())) 
    else: return list(map(int, input().split(sep)))
def ria(sep = ''): 
    return list(rip(sep))
def ri(): return int(input())
def rd(): return float(input())
def rs(): return input()
##
class union_find:
    def __init__(self, n):
        self.N = n
        self._parent = [i for i in range(self.N)]
        self._mem = [1] * self.N
        self.compo = self.N

    def parent(self, a):
        if self._parent[a] == a:
            return a
        self._parent[a] = self.parent(self._parent[a])
        return self._parent[a]

    def united(self,a, b):
        return self.parent(a) == self.parent(b)
    
    def unite(self,a, b):
        a = self.parent(a)
        b = self.parent(b)
        if(a == b): return False
        if self._mem[a] > self._mem[b]: a, b = b, a
        self._parent[a] = b
        self._mem[b] += self._mem[a]
        self.compo -= 1
        return True
    
    def is_root(self,a):
        return a == self._parent[a]
    def mem_cnt(self,a):
        return self._mem[self.parent(a)]
    def dump(self):
        print((self._parent))



def main():
    N = ri()
    X = [0] * N
    Y = [0] * N
    for i in range(N):
        X[i], Y[i] = rip()
    
    uf = union_find(N)
    di = dict()
    for i in range(N):
        if not X[i] in di: di[X[i]] = i
        uf.unite(i, di[X[i]])
    di.clear()
    for i in range(N):
        if not Y[i] in di: di[Y[i]] = i
        uf.unite(i, di[Y[i]])

    hx = [set() for i in range(N)]
    hy = [set() for i in range(N)]
    for i in range(N):
        hx[uf.parent(i)].add(X[i])
        hy[uf.parent(i)].add(Y[i])
    
    tot = 0
    for i in range(N):
        tot += len(hx[i]) * len(hy[i])
    
    print((tot - N))



def __starting_point():
    main()

__starting_point()
