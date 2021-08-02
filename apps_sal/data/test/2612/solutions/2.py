for _ in range(int(input())):
    n = int(input())
    ar = [0] + list(map(int, input().split()))
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = max(1, dp[i])
        for j in range(i + i, n + 1, i):
            if ar[j] > ar[i]:
                dp[j] = max(dp[j], dp[i] + 1)
    print(max(dp))
