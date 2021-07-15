import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,copy,functools
import random

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


def main():
    n = I()
    aa = [LI() for _ in range(n)]
    a = []
    b = []
    for i in range(1,n+1):
        c,d = aa[i-1]
        if c < d:
            a.append((c,i))
        else:
            b.append((c,i))

    if len(a) >= len(b):
        a.sort(key=lambda x: -x[0])
        r = a
    else:
        b.sort(key=lambda x: x[0])
        r = b

    return '{}\n{}'.format(len(r),' '.join(map(lambda x: str(x[1]), r)))


print(main())


