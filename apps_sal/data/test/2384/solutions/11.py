n = int(input())
a = list(map(int, input().split()))
if n % 2 == 0:
    ans, cnt = 0, 0
    for i in range(n):
        if i % 2 == 1:
            ans += a[i]
            cnt += a[i]
    for i in range(n):
        if i % 2 == 0:
            cnt += a[i]
        else:
            cnt -= a[i]
            ans = max(cnt, ans)
else:
    a.insert(0, 0)
    dp = [[0] * (n + 1) for _ in range(3)]
    for i in range(3):
        for j in range(1 + i, n + i - 1, 2):
            if i == 0:
                if j == 1:
                    dp[i][j] = a[j]
                else:
                    dp[i][j] = dp[i][j - 2] + a[j]
            else:
                dp[i][j] = max(dp[i - 1][j - 1], dp[i][j - 2] + a[j])
    ans = dp[2][n]
print(ans)
