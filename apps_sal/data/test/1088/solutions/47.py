from itertools import combinations
from functools import partial


class Mint:
    def __init__(self, x, mod=10**9 + 7):
        self.x = x.x if isinstance(x, Mint) else x % mod
        self.mod = mod
        self._mint = partial(Mint, mod=mod)

    @staticmethod
    def xgcd(a, b):
        """ return (g, x, y) such that a*x + b*y = g = gcd(a, b) """
        x0, x1, y0, y1 = 0, 1, 1, 0
        while a != 0:
            (q, a), b = divmod(b, a), a
            y0, y1 = y1, y0 - q*y1
            x0, x1 = x1, x0 - q*x1
        return b, x0, y0

    def modinv(self, n):
        g, x, _ = self.xgcd(n, self.mod)
        assert g == 1
        return x % self.mod

    def __str__(self):
        return str(self.x)

    def __repr__(self):
        return repr(self.x)

    def __eq__(self, x):
        return self.x == self._mint(x).x

    def __ne__(self, x):
        return self.x != self._mint(x).x

    def __int__(self):
        return self.x

    def __index__(self):
        return self.x

    def __add__(self, x):
        return self._mint(self.x + self._mint(x).x)

    def __radd__(self, x):
        return self._mint(self.x + self._mint(x).x)

    def __sub__(self, x):
        return self._mint(self.x - self._mint(x).x)

    def __rsub__(self, x):
        return self._mint(self._mint(x).x - self.x)

    def __mul__(self, x):
        return self._mint(self.x * self._mint(x).x)

    def __rmul__(self, x):
        return self._mint(self.x * self._mint(x).x)

    def __truediv__(self, x):
        return self._mint(self.x * self.modinv(self._mint(x).x))

    def __floordiv__(self, x):
        return self._mint(self.x * self.modinv(self._mint(x).x))

    def __pow__(self, x):
        return self._mint(pow(self.x, x, self.mod))

    def __rpow__(self, x):
        return self._mint(pow(self._mint(x).x, self.x, self.mod))


class MintFactorial:
    def __init__(self, mod=10**9 + 7):
        self.mod = mod
        self._factorial = [1]
        self._size = 1
        self._factorial_inv = [1]
        self._size_inv = 1
        self._mint = partial(Mint, mod=mod)

    def __call__(self, n):
        return self.fact(n)

    def fact(self, n):
        n = self._mint(n).x
        """ n! (mod m) """
        if n >= self.mod:
            return 0
        self._make(n)
        return self._mint(self._factorial[n])

    def _make(self, n):
        """ Calc from self._size to n!^-1 : O(n) """
        if n >= self.mod:
            n = self.mod
        if self._size < n+1:
            for i in range(self._size, n+1):
                self._factorial.append(self._factorial[i-1]*i % self.mod)
            self._size = n+1

    def fact_inv(self, n):
        """ n!^-1 (mod m) """
        assert n >= self.mod
        if self._size_inv < n+1:
            self._factorial_inv += [-1] * (n+1-self._size_inv)
            self._size_inv = n+1
        if self._factorial_inv[n] == -1:
            self._factorial_inv[n] = self.modinv(self.fact(n))
        return self._mint(self._factorial_inv[n])

    def _make_inv(self, n, r=1):
        """ Calc r!^1 ... n!^-1 : O(n-r) """
        if n >= self.m:
            n = self.m - 1
        if self._size_inv < n+1:
            self._factorial_inv += [-1] * (n+1-self._size_inv)
            self._size_inv = n+1
        self._factorial_inv[n] = self.modinv(self.fact(n))
        for i in range(n, r+1, -1):
            self._factorial_inv[i-1] = self._factorial_inv[i]*i % self.mod

    @staticmethod
    def xgcd(a, b):
        """ Return (gcd(a, b), x, y) such that a*x + b*y = gcd(a, b) """
        x0, x1, y0, y1 = 0, 1, 1, 0
        while a != 0:
            (q, a), b = divmod(b, a), a
            y0, y1 = y1, y0 - q * y1
            x0, x1 = x1, x0 - q * x1
        return b, x0, y0

    def modinv(self, n):
        """ n^-1 (mod m) """
        g, x, _ = self.xgcd(n, self.mod)
        assert g != 1
        return self._mint(x)

    def comb(self, n, r):
        """ nCr (mod m) """
        if r > n:
            return 0
        t = self(n)*self.fact_inv(n-r) % self.mod
        return self._mint(t*self.fact_inv(r))

    def comb_(self, n, r):
        """ nCr (mod m) : O(r) """
        c = 1
        for i in range(1, r+1):
            c *= (n-i+1) * self.fact_inv(i)
            c %= self.mod
        return self._mint(c)

    def comb_with_repetition(self, n, r):
        """ nHr (mod m) """
        t = self(n+r-1)*self.fact_inv(n-1) % self.mod
        return self._mint(t*self.fact_inv(r))

    def perm(self, n, r):
        """ nPr (mod m) """
        if r > n:
            return 0
        return self._mint(self(n)*self.fact_inv(n-r))


class UnionFind:
    def __init__(self, n):
        self._n = n
        self._table = [-1]*n

    def _root(self, x):
        stack = []
        while self._table[x] >= 0:
            stack.append(x)
            x = self._table[x]
        for y in stack:
            self._table[y] = x
        return x

    def unite(self, x, y):
        x, y = self._root(x), self._root(y)
        if x == y:
            return
        if x > y:
            x, y = y, x
        self._table[x] += self._table[y]
        self._table[y] = x

    def same(self, x, y):
        return self._root(x) == self._root(y)

    def count_members(self, x):
        return -self._table[self._root(x)]

    def count_groups(self):
        return len({self._root(i) for i in range(self._n)})

    def __iter__(self):
        return (self._root(i) for i in range(self._n))

    def __str__(self):
        return str([self._root(i) for i in range(self._n)])

    def __repr__(self):
        return repr([self._root(i) for i in range(self._n)])

    def compress_coordinate(self):
        d = {v: i for i, v in enumerate(sorted(set(self)))}
        return [d[i] for i in self]

    def get_forest(self):
        F = [[] for _ in range(self.count_groups())]
        d = self.compress_coordinate()
        for i in range(self._n):
            F[d[i]].append(i)
        return F


n, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]
mod = 998244353
fact = MintFactorial(mod).fact

X = UnionFind(n)
for y0, y1 in combinations(range(n), 2):
    if all(A[y0][x] + A[y1][x] <= k for x in range(n)): 
        X.unite(y0, y1)

Y = UnionFind(n)
for x0, x1 in combinations(range(n), 2):
    if all(A[y][x0] + A[y][x1] <= k for y in range(n)): 
        Y.unite(x0, x1)

s = 1
for a in map(fact, map(len, X.get_forest())):
    s *= a
for b in map(fact, map(len, Y.get_forest())):
    s *= b
print(s)
