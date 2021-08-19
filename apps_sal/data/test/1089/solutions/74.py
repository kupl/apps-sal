def main():
    (N, M, K) = list(map(int, input().split()))
    m = 10 ** 9 + 7
    ans = 0
    for d in range(1, M):
        ans += d * (M - d) % m * pow(N, 2, m) % m
        ans %= m
    for d in range(1, N):
        ans += d * (N - d) % m * pow(M, 2, m) % m
        ans %= m
    for r in range(K - 2):
        ans *= ((N * M % m - 2) % m - r) % m
        ans %= m
        ans *= pow(r + 1, m - 2, m)
        ans %= m
    print(ans)


def __starting_point():
    main()


__starting_point()
