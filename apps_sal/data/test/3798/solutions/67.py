#!usr/bin/env python3
from collections import defaultdict,deque
from heapq import heappush, heappop
import sys
import math
import bisect
import random
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def I(): return int(sys.stdin.readline())
def LS():return [list(x) for x in sys.stdin.readline().split()]
def S():
    res = list(sys.stdin.readline())
    if res[-1] == "\n":
        return res[:-1]
    return res
def IR(n):
    return [I() for i in range(n)]
def LIR(n):
    return [LI() for i in range(n)]
def SR(n):
    return [S() for i in range(n)]
def LSR(n):
    return [LS() for i in range(n)]

sys.setrecursionlimit(1000000)
mod = 1000000007

def solve():
    def f(n,b):
        if n < b:
            return n
        return f(n//b, b)+(n%b)
    n,s = IR(2)
    if n == s:
        print((n+1))
        return
    for b in range(2,10**6+2):
        if f(n,b) == s:
            print(b)
            return
    if n <= 10**6:
        print((-1))
        return
    N = 10**6+1
    for i in range(1,N)[::-1]:
        l = (n//(i+1))+1
        r = (n//i)+1
        while r-l > 1:
            m = (l+r) >> 1
            fx = f(n,m)
            if fx >= s:
                l = m
            else:
                r = m
        if f(n,l) == s:
            print(l)
            return
    print((-1))
    return

#Solve
def __starting_point():
    solve()

__starting_point()
