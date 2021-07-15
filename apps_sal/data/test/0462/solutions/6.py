import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time

sys.setrecursionlimit(10**7)
inf = 10**10
mod = 10**9 + 7

def f():
    a = list(map(int, input().split()))
    a.sort()

    return a[1] - a[0] + a[2] - a[1]

print(f())

