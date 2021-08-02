class Combination:
    def __init__(self, n, mod):
        self.fact = [1]
        for i in range(1, n + 1):
            self.fact.append(self.fact[-1] * i % mod)
        self.inv_fact = [0] * (n + 1)
        self.inv_fact[n] = pow(self.fact[n], mod - 2, mod)
        for i in reversed(list(range(n))):
            self.inv_fact[i] = self.inv_fact[i + 1] * (i + 1) % mod
        self.mod = mod

    def factorial(self, k):

        return self.fact[k]

    def inverse_factorial(self, k):
        return self.inv_fact[k]

    def permutation(self, k, r):
        if k < r:
            return 0
        return (self.fact[k] * self.inv_fact[k - r]) % self.mod

    def combination(self, k, r):
        if k < r:
            return 0
        return (self.fact[k] * self.inv_fact[k - r] * self.inv_fact[r]) % self.mod

    def combination_large(self, k, r):
        if k < r:
            return 0
        res = 1
        for l in range(r):
            res *= (k - l)
            res %= self.mod
        return (res * self.inv_fact[r]) % self.mod


n, m, k = list(map(int, input().split()))
mod = 998244353
cmb = Combination(10**6, mod)

ans = 0
for i in range(k + 1):
    ans += m * cmb.combination(n - 1, i) * pow(m - 1, n - 1 - i, mod)
    ans %= mod
print(ans)
