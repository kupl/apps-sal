import os, sys, bisect, copy
from collections import defaultdict, Counter, deque
from functools import lru_cache   #use @lru_cache(None)
if os.path.exists('in.txt'): sys.stdin=open('in.txt','r')
if os.path.exists('out.txt'): sys.stdout=open('out.txt', 'w')
#
def input(): return sys.stdin.readline()
def mapi(arg=0): return list(map(int if arg==0 else str,input().split()))
#------------------------------------------------------------------
import sys
sys.setrecursionlimit(10**5)
from types import GeneratorType
#use:- put @bootstrap overrecursive function
def bootstrap(func, stack=[]):
    def wrapped_function(*args, **kwargs):
        if stack:
            return func(*args, **kwargs)
        else:
            call = func(*args, **kwargs)
            while True:
                if type(call) is GeneratorType:
                    stack.append(call)
                    call = next(call)
                else:
                    stack.pop()
                    if not stack:
                        break
                    call = stack[-1].send(call)
            return call
    return wrapped_function

n = int(input())
gr = defaultdict(list)
for i in range(n-1):
    x,y = mapi()
    gr[x].append(y)
    gr[y].append(x)

sz = [0]*(n+1)
res = 0
@bootstrap
def dfs(s,par):
    nonlocal res
    sz[s] = 1
    for u in gr[s]:
        if par==u: continue
        sz[s]+= yield dfs(u,s)
    if sz[s]%2==0 and s!=1:
        res+=1
    yield sz[s]
dfs(1,-1)
#print(*sz)
if sz[1]&1:
    print(-1)
else:
    print(res)

