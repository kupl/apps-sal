'''
研究室PCでの解答
'''
import math
#import numpy as np
import queue
import bisect
from collections import deque,defaultdict
import heapq as hpq
from sys import stdin,setrecursionlimit
#from scipy.sparse.csgraph import dijkstra
#from scipy.sparse import csr_matrix
ipt = stdin.readline
setrecursionlimit(10**7)
mod = 10**9+7
dir = [(-1,0),(1,0),(0,-1),(0,1)]
alp = "abcdefghijklmnopqrstuvwxyz"

def rev(n,mod=(10**9+7)):
    ni = n
    nm = 1
    m2 = mod-2
    while m2 > 0:
        if m2&1:
            nm = (nm*ni)%mod
        m2 >>= 1
        ni = (ni**2)%mod
    return nm

#素因数分解
def factorization(n):
    d = dict()
    ni = n
    pn = 2
    t = 0
    while pn**2 <= n and ni > 1:
        if ni%pn == 0:
            t += 1
            ni //= pn
        else:
            if not t == 0:
                d[pn] = t
                t = 0
            if pn == 2:
                pn = 3
            else:
                pn += 2
    if t > 0:
        d[pn] = t
    if ni > 1:
        d[ni] = 1
    return d

def main():
    n = int(ipt())
    ans = 0
    a = [int(i) for i in ipt().split()]
    d = defaultdict(int)
    for i in a:
        ans += rev(i)
        di = factorization(i)
        for ki,vi in list(di.items()):
            d[ki] = max(d[ki],vi)
        ans %= mod

    for ki,vi in list(d.items()):
        ans *= pow(ki,vi,mod)
        ans %= mod

    print(ans)

    return None

def __starting_point():
    main()

__starting_point()
