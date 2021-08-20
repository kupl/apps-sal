def __starting_point():
    (n, dist) = list(map(int, input().split()))
    light = input().strip()
    right_cover = 0
    left_most = [-1] * n
    for (idx, ele) in enumerate(light):
        if ele == '1':
            for i in range(max(right_cover, idx - dist), min(idx + dist + 1, n)):
                left_most[i] = idx
            right_cover = idx + dist + 1
    dp = [0] * (2 * n + 1)
    for i in range(n):
        dp[i] = 1000000000000000000
    for idx in range(n - 1, -1, -1):
        dp[idx] = min(dp[idx + 1] + idx + 1, dp[idx])
        if left_most[idx] != -1:
            left = left_most[idx]
            dp[max(left - dist, 0)] = min(dp[idx + 1] + left + 1, dp[max(left - dist, 0)])
            dp[idx] = min(dp[max(left - dist, 0)], dp[idx])
    print(dp[0])


__starting_point()
