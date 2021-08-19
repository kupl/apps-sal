import sys
import numpy as np
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines


def fact_table(N, mod):
    inv = np.empty(N, np.int64)
    inv[0] = 0
    inv[1] = 1
    for n in range(2, N):
        (q, r) = divmod(mod, n)
        inv[n] = inv[r] * -q % mod
    fact = np.empty(N, np.int64)
    fact[0] = 1
    for n in range(1, N):
        fact[n] = n * fact[n - 1] % mod
    fact_inv = np.empty(N, np.int64)
    fact_inv[0] = 1
    for n in range(1, N):
        fact_inv[n] = fact_inv[n - 1] * inv[n] % mod
    return (fact, fact_inv, inv)


def main():
    (n, m) = list(map(int, readline().split()))
    mod = 10 ** 9 + 7
    (fact, fact_inv, inv) = fact_table(n + 1, mod)
    comb = fact[n] * fact_inv % mod * fact_inv[::-1] % mod
    comb[1::2] *= -1
    comb = comb[::-1]
    p = 1
    ans = 0
    for k in range(n + 1):
        ans += comb[k] * p % mod
        if k != n:
            p = p * (m - n + 1 + k) % mod
    ans %= mod
    print(p * ans % mod)
    return


main()
