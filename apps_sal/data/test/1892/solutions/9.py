n = int(input())
ar = []
dp = [0] * 5005
cum = [0] * 5005
mod = int(1000000000.0 + 7)
for i in range(n):
    s = input()
    ar.append(s)
for i in range(5000):
    dp[i] = 1
    cum[i] = dp[i] + (cum[i - 1] if i > 0 else 0)
    cum[i] = cum[i] - mod if cum[i] >= mod else cum[i]
for i in range(n - 2, -1, -1):
    for j in range(5000):
        dp[j] = dp[j + 1] if ar[i] == 'f' else cum[j]
        dp[j] = dp[j] - mod if dp[j] >= mod else dp[j]
        cum[j] = dp[j] + (cum[j - 1] if j > 0 else 0)
        cum[j] = cum[j] - mod if cum[j] >= mod else cum[j]
print(dp[0])
