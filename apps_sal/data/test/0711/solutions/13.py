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


def gen(n):
    x = n
    d = 2
    cnt = 0
    while x % d == 0:
        x //= d
        cnt += 1
    yield cnt

    d = 3
    ma = d * d
    while ma <= n:
        cnt = 0
        while x % d == 0:
            x //= d
            cnt += 1
        yield cnt
        ma += d * 4 + 4
        d += 2

    if x > 1:
        yield 1


def main():
    MOD = 10 ** 9 + 7

    N, M = list(map(int, input().split()))

    cal = Calc(max_value=N + 30, mod=MOD)

    ans = 1
    for cnt in gen(M):
        ans = (ans * cal.combination(N + cnt - 1, cnt)) % MOD
    print(ans)


def __starting_point():
    main()


__starting_point()
