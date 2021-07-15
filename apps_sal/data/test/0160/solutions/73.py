import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,copy,functools
import time,random

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 10**9+7
mod2 = 998244353
dd = [(-1,0),(0,1),(1,0),(0,-1)]
ddn = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(): return [list(map(int, l.split())) for l in sys.stdin.readlines()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
def pf(s): return print(s, flush=True)
def pe(s): return print(str(s), file=sys.stderr)
def JA(a, sep): return sep.join(map(str, a))
def JAA(a, s, t): return s.join(t.join(map(str, b)) for b in a)


def main():
    n,k = LI()
    a = LI()
    s = sum(a)
    dv = set([1,s])
    for i in range(2,int(s**0.5)+5):
        if s%i == 0:
            dv.add(i)
            dv.add(s//i)

    def f(i):
        pm = []
        for c in a:
            t = c % i
            if t == 0:
                continue
            pm.append((i-t, t))
        pm.sort()
        p = pi = m = 0
        mi = len(pm) - 1
        while pi <= mi:
            if p < m:
                p += pm[pi][0]
                pi += 1
            else:
                m += pm[mi][1]
                mi -= 1
        return max(p,m) <= k

    r = 1
    for c in dv:
        if f(c):
            if r < c:
                r = c

    return r


print(main())




