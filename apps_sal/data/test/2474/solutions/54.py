#!/usr/bin/env python3
import sys
INF = float("inf")

MOD = 1000000007  # type: int


class Combination(object):

    def __init__(self, N, mod=MOD):
        fac, finv, inv = [0] * (N + 1), [0] * (N + 1), [0] * (N + 1)
        fac[:2] = 1, 1
        finv[:2] = 1, 1
        inv[1] = 1
        for i in range(2, N + 1):
            fac[i] = fac[i - 1] * i % mod
            inv[i] = -inv[mod % i] * (mod // i) % mod
            finv[i] = finv[i - 1] * inv[i] % mod
        self.N = N
        self.MOD = mod
        self.fac = fac
        self.finv = finv
        self.inv = inv

    def __call__(self, n, k):
        if n < k:
            return 0
        if n < 0 or k < 0:
            return 0
        fac = self.fac
        finv = self.finv
        mod = self.MOD
        return fac[n] * (finv[k] * finv[n - k] % mod) % mod


def solve(N: int, C: "List[int]"):

    ans = 0
    C.sort(reverse=True)
    for i, c in enumerate(C, start=1):
        b = c * (pow(2, 2 * N - 2, MOD) * (i + 1)) % MOD
        ans += b
        ans %= MOD
    print((ans % MOD))
    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    C = [int(next(tokens)) for _ in range(N)]  # type: "List[int]"
    solve(N, C)


def __starting_point():
    main()


__starting_point()
