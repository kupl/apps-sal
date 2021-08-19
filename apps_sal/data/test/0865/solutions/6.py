def main():
    import numpy as np
    (n, t) = map(int, input().split())
    F = [tuple(map(int, input().split())) for _ in range(n)]
    F.sort(key=lambda x: x[0])
    dp = np.zeros([n + 1, t], dtype=np.int64)
    for i in range(n):
        a1 = F[i][0]
        b1 = F[i][1]
        dp[i + 1][:a1] = dp[i][:a1]
        dp[i + 1][a1:] = np.maximum(dp[i][a1:], dp[i][:-a1] + b1)
    ans = 0
    for i in range(n):
        ans = max(ans, dp[i][-1] + F[i][1])
    print(ans)


def __starting_point():
    main()


__starting_point()
