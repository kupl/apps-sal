#!/usr/bin/env python3

M = 998244353
fact = None
factr = None

def comb(n, k):
    if n <= 0 or k < 0 or n < k:
        return 0
    r = fact[n] * factr[k] % M
    r *= factr[n - k]
    r %= M
    return r


def solve(k, n):
    nonlocal fact, factr

    inv = [1] * (k + n + 1)
    for i in range(2, k + n + 1):
        inv[i] = inv[M % i] * (M - M // i) % M
    fact = [1] * (k + n + 1)
    factr = [1] * (k + n + 1)
    for i in range(2, k + n + 1):
        fact[i] = fact[i - 1] * i % M
        factr[i] = factr[i - 1] * inv[i] % M

    if k == 1:
        print((0))
        return
    if k == 2:
        for _ in range(3):
            print((2))
        return


    g0 = (comb(k + n - 2, k - 2) + comb(k + n - 3, k - 2)) % M
    g1 = comb(k + n - 1, k - 1)

    rs0 = [0] * (min(k // 2, n // 2) + 1)
    rs1 = [0] * (min(k // 2, n // 2) + 1)
    for t in range(1, min(k // 2, n // 2) + 1):
        rs0[t] = (comb(k + n - 2 * t - 2, k - 2) + comb(k + n - 2 * t - 3, k - 2)) % M
        rs1[t] = comb(k + n - 2 * t - 1, k - 1)

    results = [0] * (k + 2)

    for i in range(2, k + 2):
        ns = (i - 1) // 2
        ans = g0 if i % 2 == 0 else g1
        p = -1
        for t in range(1, min(ns, n // 2) + 1):
            r = rs0[t] if i % 2 == 0 else rs1[t]
            r *= comb(ns, t)
            r %= M
            ans += M + p * r
            ans %= M
            p = 0 - p
        print(ans)
        results[i] = ans
    for i in range(k + 2, 2 * k + 1):
        print((results[2 * k + 2 - i]))


def main():
    k, n = input().split()
    k = int(k)
    n = int(n)

    solve(k, n)


def __starting_point():
    main()


__starting_point()
