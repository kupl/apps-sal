MOD = 10**9 + 7

class Combination:
    def __init__(self, size, MOD):
        self.size = size + 2

        f = 1
        self.fact = fact = [f]
        for i in range(1, size+1):
            f = f * i % MOD
            fact.append(f)
        f = pow(f, MOD-2, MOD)
        self.factInv = factInv = [f]
        for i in range(size, 0, -1):
            f = f * i % MOD
            factInv.append(f)
        factInv.reverse()

    def npr(self, n, r):
        if n < r or n < 0 or r < 0:
            return 0
        return self.fact[n] * self.factInv[n - r] % MOD

    def ncr(self, n, r):
        if n < r or n < 0 or r < 0:
            return 0
        return self.fact[n] * (self.factInv[r] * self.factInv[n - r] % MOD) % MOD

    def nhr(self, n, r):  # 重複組合せ: x_1 + ... + x_n = r
        return self.ncr(n + r - 1, n - 1)

def sol():
    K = int(input())
    S = input()
    N = len(S)

    comb = Combination(N + K + 100, MOD)

    ans = 0
    L = 1
    R = pow(26, K, MOD)
    inv26 = pow(26, MOD - 2, MOD)
    for l in range(K + 1):
        ans += L * comb.nhr(N, l) * R
        ans %= MOD

        L = L * 25 % MOD
        R = R * inv26 % MOD

    print(ans)
sol()
