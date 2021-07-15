#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**8)
INF = float("inf")

MOD = 1000000007  # type: int


class Combination(object):

    def __init__(self, N, mod=MOD):
        fac, finv, inv = [0]*(N+1), [0]*(N+1), [0]*(N+1)
        fac[:2] = 1, 1
        finv[:2] = 1, 1
        inv[1] = 1
        for i in range(2, N+1):
            fac[i] = fac[i-1]*i % mod
            inv[i] = -inv[mod % i]*(mod//i) % mod
            finv[i] = finv[i-1]*inv[i] % mod
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
        return fac[n] * (finv[k]*finv[n-k] % mod) % mod


def solve(H: int, W: int, A: int, B: int):

    cmb = Combination(H+W+1, MOD)

    ans = 0
    for i in range(B, W):
        buf = cmb(H-A-1+i, i)
        buf *= cmb(A+W-i-2, W-i-1)
        buf %= MOD
        ans += buf
        ans %= MOD
    print(ans)

    return


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    H = int(next(tokens))  # type: int
    W = int(next(tokens))  # type: int
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    solve(H, W, A, B)


def __starting_point():
    main()

__starting_point()
