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


def main():
    MOD = 10 ** 9 + 7

    N, M, K = list(map(int, input().split()))

    calc = Calc(max_value=N * M - 2, mod=MOD)

    xsum = 0
    for d in range(1, N):
        xsum = (xsum + d * (N - d)) % MOD
    xsum = (xsum * M * M) % MOD

    ysum = 0
    for d in range(1, M):
        ysum = (ysum + d * (M - d)) % MOD
    ysum = (ysum * N * N) % MOD

    ans = (xsum + ysum) * calc.combination(N * M - 2, K - 2) % MOD

    print(ans)


def __starting_point():
    main()


__starting_point()
