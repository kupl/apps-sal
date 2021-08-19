from fractions import Fraction
from collections import defaultdict
from itertools import combinations


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


N = int(input())
XY = [list(map(int, input().split())) for i in range(N)]

D = defaultdict(int)
for (x1, y1), (x2, y2) in combinations(XY, 2):
    if x1 != x2:
        a = Fraction(y2 - y1, x2 - x1)
        b = Fraction(y1) - a * Fraction(x1)
        D[(a, b)] += 1
    else:
        D[(None, x1)] += 1

mod = 998244353
comb = Combination(N + 1, mod)
A = [0] * (N + 1)
coA = [0] * (N + 1)
ans = 0
for i in range(3, N + 1):
    ans += comb(N, i)
    ans %= mod
for i in range(3, N + 1):
    for j in range(i - 2):
        A[i] += (i - 2 - j) * (1 << j)
    coA[i] = coA[i - 1] + A[i]
for (a, b), n in D.items():
    if n == 1:
        continue
    n = int((n << 1)**0.5) + 1
    ans -= coA[n]
    ans %= mod
print(ans)
