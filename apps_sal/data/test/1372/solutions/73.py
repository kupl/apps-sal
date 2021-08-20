def main():
    (H, N) = list(map(int, input().split()))
    ab = []
    for _ in range(N):
        ab.append(list(map(int, input().split())))
    dp = [0] * (H + max([a for (a, _) in ab]))
    for i in range(1, H + 1):
        dp[i] = min([dp[i - a] + b for (a, b) in ab])
    print(dp[H])


def __starting_point():
    main()


__starting_point()
