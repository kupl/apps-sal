t = int(input())

for _ in range(t):
    n,p,k = map(int, input().split())
    a = list(map(int, input().split()))
    a = sorted(a)

    dp = [10**10 for i in range(n+1)]
    dp[0] = 0

    for i in range(1, n+1):
        dp[i] = min(dp[i], dp[i-1] + a[i-1])
        if i >= k:
            dp[i] = min(dp[i], dp[i-k] + a[i-1])
    ans = 0
    for i in range(n+1):
        if dp[i] <= p:
            ans = i
    print(ans)
