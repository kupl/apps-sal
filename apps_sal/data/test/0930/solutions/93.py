import sys
input = sys.stdin.readline

MOD = 10 ** 9 + 7


def main():
    N, K = (int(_) for _ in input().split())

    fact = [0] * (N + 1)
    ifact = [0] * (N + 1)

    for i in range(N + 1):
        if i == 0:
            fact[i] = 1
            continue
        fact[i] = i * fact[i - 1]
        fact[i] %= MOD
    ifact[N] = pow(fact[N], MOD - 2, MOD)
    for i in range(N)[::-1]:
        ifact[i] = ((i + 1) * ifact[i + 1]) % MOD

    ret = 0
    for m in range(min(K, N - 1) + 1):
        ret += (fact[N] * ifact[m] * ifact[N - m]) % MOD * (fact[N - 1] * ifact[N - m - 1] * ifact[m]) % MOD
        ret %= MOD
    print((ret % MOD))

    return


def __starting_point():
    main()


__starting_point()
