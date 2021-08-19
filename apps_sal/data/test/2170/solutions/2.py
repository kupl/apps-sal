import sys
import math
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline


def main():
    (N, M) = [int(x) for x in input().split()]
    MOD = 10 ** 9 + 7
    fact = [1, 1]
    factinv = [1, 1]
    inv = [0, 1]

    def cmb(n, k, p):
        if k < 0 or n < k:
            return 0
        r = min(k, n - k)
        return fact[n] * factinv[k] * factinv[n - k] % p
    for i in range(2, 10 ** 6 + 1):
        fact.append(fact[-1] * i % MOD)
        inv.append(-inv[MOD % i] * (MOD // i) % MOD)
        factinv.append(factinv[-1] * inv[-1] % MOD)
    X = fact[M] * factinv[M - N]
    ans = 0
    for i in range(N + 1):
        c = fact[M - i] * factinv[M - i - (N - i)]
        if i % 2 == 0:
            ans += X * c * cmb(N, i, MOD)
        else:
            ans -= X * c * cmb(N, i, MOD)
        ans %= MOD
    print(ans % MOD)


def __starting_point():
    main()


__starting_point()
