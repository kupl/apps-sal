import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,copy,functools
import time

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 10**9+7
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
    n = I()
    a = sorted(LI())
    q = [a[-1]]
    a = a[:-1][::-1]
    for i in range(n):
        # print(i,q,a)
        nq = []
        qi = 0
        na = []
        for ai in range(len(a)):
            c = a[ai]
            if q[qi] > c:
                nq.append(c)
                qi += 1
                if qi == len(q):
                    na += a[ai+1:]
                    break
            else:
                na.append(c)
        if qi < len(q):
            return 'No'
        a = na
        q = sorted(q + nq, reverse=True)

    return 'Yes'


print(main())


