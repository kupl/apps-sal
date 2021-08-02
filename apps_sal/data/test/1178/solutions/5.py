def solve():
    INF = float('inf')

    def max2(x, y): return x if x >= y else y

    N, K = list(map(int, input().split()))
    Hs = [0] + list(map(int, input().split()))

    if N == K:
        return 0

    dp = [INF] * (N + 1)
    dp[0] = 0
    for j in range(1, N - K + 1):
        dp2 = [INF] * (N + 1)
        for i, H in enumerate(Hs[j:], j):
            for k in range(j - 1, i):
                dp2[i] = min(dp2[i], dp[k] + max2(0, H - Hs[k]))
        dp = dp2

    return min(dp)


ans = solve()
print(ans)
