MOD = 10**9 + 7


class Combination:
    def __init__(self, size):
        self.size = size + 2
        self.fact = [1, 1] + [0] * size
        self.factInv = [1, 1] + [0] * size
        self.inv = [0, 1] + [0] * size

        for i in range(2, self.size):
            self.fact[i] = self.fact[i - 1] * i % MOD
            self.inv[i] = -self.inv[MOD % i] * (MOD // i) % MOD
            self.factInv[i] = self.factInv[i - 1] * self.inv[i] % MOD

    def npr(self, n, r):
        if n < r or n < 0 or r < 0:
            return 0
        return self.fact[n] * self.factInv[n - r] % MOD

    def ncr(self, n, r):
        if n < r or n < 0 or r < 0:
            return 0
        return self.fact[n] * (self.factInv[r] * self.factInv[n - r] % MOD) % MOD

    def nhr(self, n, r):
        return self.ncr(n + r - 1, n - 1)


N, M = list(map(int, input().split()))
comb = Combination(N + 100)


def primeCount(N):
    R = int(N**(0.5)) + 1
    primes = {}
    n = N
    for num in range(2, R):
        primes[num] = 0
        while n % num == 0:
            n //= num
            primes[num] += 1
    if n > 1:
        primes[n] = 1
    return {key: val for key, val in list(primes.items()) if val > 0}


ans = 1
for c in list(primeCount(M).values()):
    ans *= comb.nhr(N, c)
    ans %= MOD
print(ans)
