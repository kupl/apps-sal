import sys
sys.setrecursionlimit(10000000)
MOD = 10 ** 9 + 7
INF = 10 ** 15


def main():
    N, M, K = map(int, input().split())

    MAXN = N * M
    fact = [1]
    for i in range(1, MAXN + 1):
        fact.append(fact[-1] * i % MOD)
    inv_fact = [-1] * (MAXN + 1)
    inv_fact[-1] = pow(fact[-1], MOD - 2, MOD)
    for i in range(MAXN - 1, -1, -1):
        inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD

    def nck(N, K): return 0 if K > N or K < 0 else fact[N] * inv_fact[N - K] * inv_fact[K] % MOD

    ans = 0
    const = nck(N * M - 2, K - 2)
    for i in range(1, N):
        ans += (N - i) * M * M * const * i % MOD
        ans %= MOD

    for i in range(1, M):
        ans += (M - i) * N * N * const * i % MOD
        ans %= MOD
    print(ans)


def __starting_point():
    main()


__starting_point()
