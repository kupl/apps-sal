import sys
sys.setrecursionlimit(10**9)
INF = 10**18
MOD = 998244353
def input(): return sys.stdin.readline().rstrip()
def YesNo(b): return bool([print('Yes')] if b else print('No'))
def YESNO(b): return bool([print('YES')] if b else print('NO'))


def int1(x): return int(x) - 1


N, K = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(N)]


class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.siz = [1] * n

    def root(self, x):
        while self.par[x] != x:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x

    def unite(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return False
        if self.siz[x] < self.siz[y]:
            x, y = y, x
        self.siz[x] += self.siz[y]
        self.par[y] = x
        return True

    def is_same(self, x, y):
        return self.root(x) == self.root(y)

    def size(self, x):
        return self.siz[self.root(x)]

    def get_roots(self):
        roots = set()
        for i in range(len(self.par)):
            roots.add(self.root(i))
        return list(roots)

    def get_roots_and_size(self):
        roots = self.get_roots()
        roots_and_size = [[v, self.size(v)] for v in roots]
        return roots_and_size


uy = UnionFind(N)
ux = UnionFind(N)
for y0 in range(N):
    for y1 in range(N):
        for x in range(N):
            if a[y0][x] + a[y1][x] > K:
                break
        else:
            uy.unite(y0, y1)
for x0 in range(N):
    for x1 in range(N):
        for y in range(N):
            if a[y][x0] + a[y][x1] > K:
                break
        else:
            ux.unite(x0, x1)
ans = 0
ry = uy.get_roots_and_size()
rx = ux.get_roots_and_size()


def COMinit(n, MOD):
    fac, finv, inv = [0] * max(2, n + 1), [0] * max(2, n + 1), [0] * max(2, n + 1)
    fac[0] = fac[1] = 1
    finv[0] = finv[1] = 1
    inv[1] = 1
    for i in range(2, (n + 1)):
        fac[i] = fac[i - 1] * i % MOD
        inv[i] = MOD - inv[MOD % i] * (MOD // i) % MOD
        finv[i] = finv[i - 1] * inv[i] % MOD
    return fac, finv, inv


fac, finv, inv = COMinit(N, MOD)


def COM(n, k, MOD=MOD):
    if n < k or n < 0 or k < 0:
        return 0
    return fac[n] * (finv[k] * finv[n - k] % MOD) % MOD


ans = 1
for _, v in ry:
    ans *= fac[v]
    ans %= MOD
for _, v in rx:
    ans *= fac[v]
    ans %= MOD
print(ans)
