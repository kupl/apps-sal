class Calc:
    def __init__(self, max_value, mod):
        """combination(max_value, all)"""
        fact = [-1] * (max_value + 1)
        fact[0] = 1
        fact[1] = 1
        for x in range(2, max_value + 1):
            fact[x] = x * fact[x - 1] % mod

        invs = [1] * (max_value + 1)
        invs[max_value] = pow(fact[max_value], mod - 2, mod)
        for x in range(max_value - 1, 0, -1):
            invs[x] = invs[x + 1] * (x + 1) % mod

        self.fact = fact
        self.invs = invs
        self.mod = mod

    def combination(self, n, r):
        if n - r < r:
            return self.combination(n, n - r)
        if r < 0:
            return 0
        if r == 0:
            return 1
        if r == 1:
            return n
        return self.fact[n] * self.invs[r] * self.invs[n - r] % self.mod

    def factorial(self, n):
        return self.fact[n]


def main():
    MOD = 10 ** 9 + 7

    N, K = list(map(int, input().split()))
    K = min(K, N - 1)  # K=最大空室数->N部屋空室は不可能

    calc = Calc(max_value=N * 2, mod=MOD)

    ans = 0
    for v in range(K + 1):  # 空室数
        ans = (ans + (calc.combination(N, v) * calc.combination(v + (N - v) - 1, v)) % MOD) % MOD

    print(ans)


def __starting_point():
    main()

__starting_point()
