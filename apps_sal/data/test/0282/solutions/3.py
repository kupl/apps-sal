(n, d) = list(map(int, input().strip().split(' ')))
arr = input()
dp = [10000 for i in range(1000)]
dp[0] = 0
i = 1
while i < n:
    if arr[i] == '1':
        for j in range(i - 1, max(-1, i - d - 1), -1):
            dp[i] = min(dp[i], dp[j] + 1)
    i += 1
if dp[n - 1] == 10000:
    print(-1)
else:
    print(dp[n - 1])
