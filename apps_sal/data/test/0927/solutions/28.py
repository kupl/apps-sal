n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
d = [10**5, 2, 5, 5, 4, 5, 6, 3, 7, 6]
dp = [(0, 0)] * (n + 1)
for i in range(n):
    if i > 0 and dp[i][0] == 0:
        continue
    k, _ = dp[i]
    for ai in a:
        if i + d[ai] <= n:
            dp[i + d[ai]] = max(dp[i + d[ai]], (k + 1, ai))
ans = []
i = n
for _ in range(dp[n][0]):
    ans.append(str(dp[i][1]))
    i -= d[dp[i][1]]
print((''.join(ans)))
