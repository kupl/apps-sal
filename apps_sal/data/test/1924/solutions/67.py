(r1, c1, r2, c2) = map(int, input().split())


class Combination:

    def __init__(self, N: int, MOD: int):
        fac = [0 for _ in range(N + 1)]
        fac[0] = 1
        for i in range(1, N + 1):
            fac[i] = fac[i - 1] * i % MOD
        self.fac = fac
        self.N = N
        self.MOD = MOD

    def _modpow(self, x: int, n: int) -> int:
        ret = 1
        while n > 0:
            if n % 2 == 1:
                ret = ret * x % self.MOD
            x = x * x % self.MOD
            n >>= 1
        return ret

    def _modinv(self, x: int) -> int:
        return self._modpow(x, self.MOD - 2)

    def combination(self, n: int, k: int) -> int:
        if n < k:
            return 0
        return self.fac[n] * self._modinv(self.fac[k]) % self.MOD * self._modinv(self.fac[n - k]) % self.MOD


MOD = 1000000007
comb = Combination(2 * 1000000 + 10, MOD)
ans = (2 * MOD + comb.combination(r1 + c1, r1) - comb.combination(r1 + c2 + 1, r1) - comb.combination(r2 + c1 + 1, r2 + 1) + comb.combination(r2 + c2 + 2, r2 + 1)) % MOD
print(ans)
