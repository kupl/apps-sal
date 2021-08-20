def inv(x, mod):
    return pow(x, mod - 2, mod)


def main() -> None:
    (N, M, K) = list(map(int, input().split()))
    MOD = 10 ** 9 + 7
    ans = 0
    for d in range(1, N):
        ans += M * M * (N - d) * d
        ans %= MOD
    for d in range(1, M):
        ans += N * N * (M - d) * d
        ans %= MOD
    for i in range(K - 2):
        ans = ans * (N * M - 2 - i) % MOD
    for i in range(K - 2):
        ans = ans * inv(i + 1, MOD) % MOD
    print(ans)


def __starting_point():
    main()


__starting_point()
