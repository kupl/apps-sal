#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10**8)
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return list(map(int, input().split()))
def LIST(): return list(map(int, input().split()))
def ZIP(n): return list(zip(*(MAP() for _ in range(n))))


INF = float("inf")
MOD = 10**9 + 7


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
        return self.C(n, k)

    def C(self, n, k):
        if n < k:
            return 0
        if n < 0 or k < 0:
            return 0
        fac = self.fac
        finv = self.finv
        mod = self.MOD
        return fac[n] * (finv[k] * finv[n - k] % mod) % mod

    def P(self, n, k):
        if n < k:
            return 0
        if n < 0 or k < 0:
            return 0
        return self.fac[n] * self.finv[n - k]


def main():
    N, M = MAP()
    ans = 0

    cmb = Combination(M)

    sign = +1
    for i in range(N + 1):
        ans += sign * cmb.P(M - i, N - i) * cmb(N, i)
        ans %= MOD
        sign *= -1
    ans *= cmb.P(M, N)
    ans %= MOD
    print(ans)
    return


def __starting_point():
    main()


__starting_point()
