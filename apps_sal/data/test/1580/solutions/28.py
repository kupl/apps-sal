# -*- coding: utf-8 -*-
import sys 
sys.setrecursionlimit(10**6)
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
#Union Find
def find(x):
    if par[x] < 0:
        return x
    else:
        par[x] = find(par[x])
        return find(par[x])

def union(x,y):
    x = find(x)
    y = find(y)
    if x==y:
        return False
    else:
        if par[x] > par[y]:
            x,y = y,x
        par[x] += par[y]
        par[y] = x
        return True

def same(x,y):
    return find(x) == find(y)        
    
N,M = map(int,readline().split())
par = [-1]*(N+1)
for i in range(M):
    x,y,z = map(int,readline().split())
    union(x,y)
print(sum(1 for i in par[1:] if i < 0))
