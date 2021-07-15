import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 998244353
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

def MF(n,d): return ModFraction(n,d)

class ModFraction():
    def __init__(self, n, d):
        self.n = n
        self.d = d

    def __add__(self, x):
        xf = ModFraction.xf(x)
        a = self.n * xf.d % mod
        b = xf.n * self.d % mod
        c = self.d * xf.d % mod
        return ModFraction((a+b) % mod, c)

    def __sub__(self, x):
        xf = ModFraction.xf(x)
        a = self.n * xf.d % mod
        b = -xf.n * self.d % mod
        c = self.d * xf.d % mod
        return ModFraction((a+b) % mod, c)

    def __mul__(self, x):
        xf = ModFraction.xf(x)
        a = self.n * xf.n % mod
        b = self.d * xf.d % mod
        return ModFraction(a, b)

    def __truediv__(self, x):
        xf = ModFraction.xf(x)
        a = self.n * xf.d % mod
        b = self.d * xf.n % mod
        return ModFraction(a, b)

    @classmethod
    def xf(cls, x):
        if isinstance(x, int):
            return ModFraction(x, 1)
        return x

    @classmethod
    def inv(cls, x):
        return pow(x, mod - 2, mod)

    def int(self):
        return self.n * ModFraction.inv(self.d) % mod

    def __str__(self):
        return "{} / {}".format(self.n, self.d)

def main():
    n,m = LI()
    a = LI()
    w = LI()

    fm = {}
    def f(c,a,m,p,q):
        if m == 0 or c == 0:
            return MF(c, 1)

        key = (c,a,m,p,q)
        if key in fm:
            return fm[key]

        s = c + p + q
        x = f(c+a,a,m-1,p,q)
        r = x * MF(c, s)
        if p > 0:
            y = f(c,a,m-1,p+1,q)
            r = r + y * MF(p, s)
        if q > 0:
            z = f(c,a,m-1,p,q-1)
            r = r + z * MF(q, s)

        fm[key] = r
        return r

    ps = 0
    qs = 0
    for i in range(n):
        if a[i] == 1:
            ps += w[i]
        else:
            qs += w[i]

    r = []
    for i in range(n):
        if a[i] == 1:
            v = f(w[i],1,m,ps-w[i],qs)
        else:
            v = f(w[i],-1,m,ps,qs-w[i])

        r.append(v.int())

    return JA(r,'\n')


print(main())


