MOD = 1000000007


class mint:

    def __init__(self, x=0):
        self.x = x % MOD

    def __str__(self):
        return str(self.x)
    __repr__ = __str__

    def __add__(self, other):
        return mint(self.x + other.x) if isinstance(other, mint) else mint(self.x + other)

    def __sub__(self, other):
        return mint(self.x - other.x) if isinstance(other, mint) else mint(self.x - other)

    def __mul__(self, other):
        return mint(self.x * other.x) if isinstance(other, mint) else mint(self.x * other)

    def __truediv__(self, other):
        return mint(self.x * pow(other.x, MOD - 2, MOD)) if isinstance(other, mint) else mint(self.x * pow(other, MOD - 2, MOD))

    def __pow__(self, other):
        return mint(pow(self.x, other.x, MOD)) if isinstance(other, mint) else mint(pow(self.x, other, MOD))
    __radd__ = __add__

    def __rsub__(self, other):
        return mint(other.x - self.x) if isinstance(other, mint) else mint(other - self.x)
    __rmul__ = __mul__

    def __rtruediv__(self, other):
        return mint(other.x * pow(self.x, MOD - 2, MOD)) if isinstance(other, mint) else mint(other * pow(self.x, MOD - 2, MOD))

    def __rpow__(self, other):
        return mint(pow(other.x, self.x, MOD)) if isinstance(other, mint) else mint(pow(other, self.x, MOD))


MAX = 1000005
fac = [1, 1]
finv = [1, 1]
inv = [0, 1]


def COMinit():
    for i in range(2, MAX):
        fac.append(fac[-1] * i % MOD)
        inv.append(-inv[MOD % i] * (MOD // i) % MOD)
        finv.append(finv[-1] * inv[-1] % MOD)


def COM(n, k):
    if n < k:
        return 0
    if n < 0 or k < 0:
        return 0
    return fac[n] * finv[k] * finv[n - k] % MOD


def P(n, k):
    return fac[n] * finv[n - k] % MOD


(N, M) = map(int, input().split())
COMinit()
res = mint(0)
now = mint()
for i in range(N + 1):
    now = COM(N, i)
    now *= P(M - i, N - i)
    if i % 2 == 1:
        now = -1 * now
    res += now
res *= P(M, N)
print(res)
