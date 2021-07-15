import math,string,itertools,collections,re,fractions,array,copy
import bisect
import heapq
from itertools import chain, dropwhile, permutations, combinations
from collections import deque, defaultdict, OrderedDict, namedtuple, Counter, ChainMap


# Guide:
#   1. construct complex data types while reading (e.g. graph adj list)
#   2. avoid any non-necessary time/memory usage
#   3. avoid templates and write more from scratch
#   4. switch to "flat" implementations

def VI(): return list(map(int,input().split()))
def I(): return int(input())
def LIST(n,m=None): return [0]*n if m is None else [[0]*m for i in range(n)]
def ELIST(n): return [[] for i in range(n)]
def MI(n=None,m=None): # input matrix of integers
    if n is None: n,m = VI()
    arr = LIST(n)
    for i in range(n): arr[i] = VI()
    return arr
def MS(n=None,m=None): # input matrix of strings
    if n is None: n,m = VI()
    arr = LIST(n)
    for i in range(n): arr[i] = input()
    return arr
def MIT(n=None,m=None): # input transposed matrix/array of integers
    if n is None: n,m = VI()
    a = MI(n,m)
    arr = LIST(m,n)
    for i,l in enumerate(a):
        for j,x in enumerate(l):
            arr[j][i] = x
    return arr

def main(info=0):
    n,k = VI()
    if k>n*n:
        print("-1")
    else:
        m = [["0" for _ in range(n)] for _ in range(n)]
        i,j = 0,0
        for i in range(n):
            for j in range(i, n):
                if k==0: break
                if i==j:
                    m[i][j] = "1"
                    k -= 1
                else:
                    if k==1: continue
                    m[i][j] = "1"
                    m[j][i] = "1"
                    k -= 2
            if k==0: break
        for l in m:
            print(" ".join(l))




def __starting_point():
    main()

__starting_point()
