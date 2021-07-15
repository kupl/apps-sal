class Enumerator:
    def __init__(self, N: int, MOD: int) -> None:
        self.fact = [1, 1]
        self.finv = [1, 1]
        self.invs = [0, 1]
        for i in range(2, N + 1):
            self.fact.append(self.fact[i - 1] * i % MOD)
            self.invs.append(-self.invs[MOD % i] * (MOD // i) % MOD)
            self.finv.append(self.finv[-1] * self.invs[-1] % MOD)
        self._MOD = MOD
        self._N = N

    def choose(self, n: int, k: int) -> int:
        if p := self.permutate(n, k):
            return p * self.finv[k] % self._MOD
        else:
            return 0

    def permutate(self, n: int, k: int) -> int:
        if n < k or n < 0 or k < 0:
            return 0
        assert n <= self._N and k <= self._N
        return self.fact[n] * self.finv[n - k] % self._MOD

    def choose_with_duplicates(self, n: int, k: int) -> int:
        return self.choose(n + k - 1, n)


N, K = list(map(int, input().split()))
A = list(map(int, input().split()))
MOD = 1_000_000_007
A.sort()
e = Enumerator(N, MOD)
nck = e.choose(N, K)
ans = 0
for i in range(N - 1):
    ci = nck - e.choose(i + 1, K) - e.choose(N - i - 1, K)
    ans += ci * (A[i + 1] - A[i])
    ans %= MOD
print(ans)

