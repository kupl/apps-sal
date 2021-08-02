from decimal import Decimal
from math import pi, gcd
from functools import reduce, lru_cache
from itertools import product, combinations
from heapq import heappop, heappush
from collections import deque, defaultdict, Counter
def LI(): return list(map(int, input().split()))
def II(): return int(input())
def LI(): return list(map(int, input().split()))
def II(): return int(input())
def yes(): return print("Yes")
def no(): return print("No")


INF = float("inf")

mod = 998244353
mod = 10**9 + 7


class Combination:
    """
    O(n)の前計算を1回行うことで，O(1)でnCr mod mを求められる
    n_max = 10**6のとき前処理は約950ms (PyPyなら約340ms, 10**7で約1800ms)
    使用例：
    comb = Combination(1000000)
    print(comb(5, 3))  # 10
    """

    def __init__(self, n_max, mod=10**9 + 7):
        self.mod = mod
        self.modinv = self.make_modinv_list(n_max)
        self.fac, self.facinv = self.make_factorial_list(n_max)

    def __call__(self, n, r):
        return self.fac[n] * self.facinv[r] % self.mod * self.facinv[n - r] % self.mod

    def make_factorial_list(self, n):
        # 階乗のリストと階乗のmod逆元のリストを返す O(n)
        # self.make_modinv_list()が先に実行されている必要がある
        fac = [1]
        facinv = [1]
        for i in range(1, n + 1):
            fac.append(fac[i - 1] * i % self.mod)
            facinv.append(facinv[i - 1] * self.modinv[i] % self.mod)
        return fac, facinv

    def make_modinv_list(self, n):
        # 0からnまでのmod逆元のリストを返す O(n)
        modinv = [0] * (n + 1)
        modinv[1] = 1
        for i in range(2, n + 1):
            modinv[i] = self.mod - self.mod // i * modinv[self.mod % i] % self.mod
        return modinv


class Unionfind:
    def __init__(self, N):
        self.p = list(range(N))
        self.rank = [0] * N
        self.size = [1] * N

    def root(self, x):
        if self.p[x] != x:
            self.p[x] = self.root(self.p[x])

        return self.p[x]

    def same(self, x, y):
        return self.root(x) == self.root(y)

    def unite(self, x, y):
        u = self.root(x)
        v = self.root(y)

        if u == v: return

        if self.rank[u] < self.rank[v]:
            self.p[u] = v
            self.size[v] += self.size[u]
            self.size[u] = 0
        else:
            self.p[v] = u
            self.size[u] += self.size[v]
            self.size[v] = 0

            if self.rank[u] == self.rank[v]:
                self.rank[u] += 1

    def count(self, x):
        return self.size[self.root(x)]


# フレンズさんの模範回答
class dsu:
    def __init__(self, n):
        self.cnt = [1] * n
        self.root = list(range(n))

    def unite(self, x, y):
        x = self.root[x]
        y = self.root[y]
        if x != y:
            if self.cnt[x] < self.cnt[y]:
                x, y = y, x
            self.cnt[x] += self.cnt[y]
            self.root[y] = x
        return x

    def leader(self, x):
        if self.root[x] == x:
            return x
        self.root[x] = self.leader(self.root[x])
        return self.root[x]


n = II()
p = LI()

ans = []
ansset = set()
ind_list = [-1] * (n + 1)
for ind, num in enumerate(p):
    ind_list[num] = ind
for i in range(1, n + 1):
    a = ind_list[i]

    while a > i - 1:
        p[a], p[a - 1] = p[a - 1], p[a]
        ind_list[p[a]] += 1
        ans.append(a)
        if a in ansset:
            print(-1)
            return
        ansset.add(a)
        a -= 1
if p == list(range(1, n + 1)):
    if len(ans) == n - 1:
        for val in ans:
            print(val)
        return

print(-1)
