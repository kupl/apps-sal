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


class Flow():
    def __init__(self, e, N):
        self.E = e
        self.N = N

    def max_flow(self, s, t):
        r = 0
        e = self.E

        def f(c, cap):
            v = self.v
            v[c] = 1
            if c == t:
                return cap
            for i in range(self.N):
                if v[i] or e[c][i] <= 0:
                    continue
                cp = min(cap, e[c][i])
                k = f(i, cp)
                if k > 0:
                    e[c][i] -= k
                    e[i][c] += k
                    return k
            return 0

        while True:
            self.v = [None] * self.N
            fs = f(s, inf)
            if fs == 0:
                break
            r += fs

        return r


def main():
    n = I()
    a = LI()

    s = n
    t = n + 1
    e = [[0] * (n+2) for _ in range(n+2)]
    for i in range(n):
        c = a[i]
        if c < 0:
            e[s][i] = -c
            ii = i + 1
            for j in range(ii*2, n+1, ii):
                e[i][j-1] = inf
        else:
            e[i][t] = c


    fl = Flow(e, n+2)
    r = fl.max_flow(s,t)

    return sum(map(lambda x: max(0,x), a)) - r

# start = time.time()
print(main())
# pe(time.time() - start)




