class Combination:
    def __init__(self, n, MOD):
        self.fact = [1]
        for i in range(1, n + 1):
            self.fact.append(self.fact[-1] * i % MOD)
        self.inv_fact = [0] * (n + 1)
        self.inv_fact[n] = pow(self.fact[n], MOD - 2, MOD)
        for i in reversed(range(n)):
            self.inv_fact[i] = self.inv_fact[i + 1] * (i + 1) % MOD
        self.MOD = MOD

    def factorial(self, k):
        return self.fact[k]

    def inverse_factorial(self, k):
        return self.inv_fact[k]

    def permutation(self, k, r):
        if k < r:
            return 0
        return (self.fact[k] * self.inv_fact[k - r]) % self.MOD

    def combination(self, k, r):
        if k < r:
            return 0
        return (self.fact[k] * self.inv_fact[k - r] * self.inv_fact[r]) % self.MOD



n, m = map(int, input().split())
MOD = 998244353
comb = Combination(2 * 10 ** 5 + 10, MOD)

ans = 0
pow_ = pow(2, n - 2, MOD)
for i in range(1, m + 1):
    tmp = comb.combination(i - 1, n - 2)
    tmp *= pow_
    tmp *= n - 2
    ans += tmp
    ans %= MOD
print(ans * pow(2, MOD - 2, MOD) % MOD)
