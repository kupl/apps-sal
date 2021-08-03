def main():
    N, T = list(map(int, input().split()))
    L = [[int(x) for x in input().split()] for _ in range(N)]
    L.sort(key=lambda x: x[0])
    dp = [0] + [-1] * (T + L[-1][0])

    for a, b in L:
        for j in range(T - 1, -1, -1):
            if dp[j] >= 0 and dp[j + a] < dp[j] + b:
                dp[j + a] = dp[j] + b

    print((max(dp)))


def __starting_point():
    main()


__starting_point()
