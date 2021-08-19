def main():
    (N, T) = list(map(int, input().split()))
    ab = [tuple(map(int, input().split())) for i in range(N)]
    ab.sort(key=lambda x: x[0])
    t = ab[-1][0]
    dp = [-1] * (T + t + 1)
    dp[0] = 0
    for (a, b) in ab:
        for i in range(T - 1, -1, -1):
            if dp[i] < 0:
                continue
            if dp[i + a] < dp[i] + b:
                dp[i + a] = dp[i] + b
    ans = max(dp)
    print(ans)


main()
