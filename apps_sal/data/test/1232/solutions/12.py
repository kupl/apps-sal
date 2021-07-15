import math,string,itertools,fractions,heapq,collections,re,array,bisect,copy
from itertools import chain, dropwhile, permutations, combinations
from collections import defaultdict, deque

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


def run(na,nb,k,m,a,b):
    if a[k-1] < b[nb-m]:
        print("YES")
    else:
        print("NO")


def main(info=0):
    na,nb = VI()
    k,m = VI()
    a = VI()
    b = VI()
    run(na,nb,k,m,a,b)



def __starting_point():
    main()

__starting_point()
