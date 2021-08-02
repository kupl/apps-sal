def solve():
    N, K = [int(i) for i in input().split()]
    ans = 0
    mod = 10**9 + 7
    for M in range(K, N + 2):
        min_sum = (M - 1) * M // 2
        max_sum = (2 * N - (M - 1)) * M // 2
        cnt = max_sum - min_sum + 1
        ans += cnt
        ans %= mod
    print(ans)


def __starting_point():
    solve()


__starting_point()
