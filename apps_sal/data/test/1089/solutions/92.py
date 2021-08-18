import sys
mod = 7 + 10 ** 9


def comb(n, r, fact, revfact):
    return (fact[n] * revfact[n - r] * revfact[r]) % mod


def solve():
    input = sys.stdin.readline
    N, M, K = map(int, input().split())
    fact = [1] * (N * M + 1)
    for i in range(1, N * M + 1):
        fact[i] = (fact[i - 1] * i) % mod
    revfact = [1] * (N * M + 1)
    revfact[N * M] = pow(fact[N * M], mod - 2, mod)
    for i in reversed(range(1, N * M)):
        revfact[i] = ((i + 1) * revfact[i + 1]) % mod

    others = comb(N * M - 2, K - 2, fact, revfact)
    pair_type = 0
    for i in range(N):
        if i == 0:
            for j in range(1, M):
                pair_type += (i + j) * (N - i) * (M - j) % mod
                pair_type %= mod
        else:
            for j in range(M):
                if j == 0:
                    pair_type += (i + j) * (N - i) * (M - j) % mod
                else:
                    pair_type += 2 * (i + j) * (N - i) * (M - j) % mod
                pair_type %= mod

    print(pair_type * others % mod)
    return 0


def __starting_point():
    solve()


__starting_point()
