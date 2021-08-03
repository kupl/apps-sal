mod = 998244353
n, k = map(int, input().split())
L = []
R = []
for _ in range(k):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)
dp = [0] * n
dp[0] = 1
dp_s = [0] * n
dp_s[0] = 1
for i in range(1, n):
    for j in range(k):
        l = L[j]
        r = R[j]
        if i - l >= 0:
            if i - r >= 1:
                dp[i] = (dp[i] + dp_s[i - l] - dp_s[i - r - 1]) % mod
            else:
                dp[i] = (dp[i] + dp_s[i - l]) % mod
    dp_s[i] = (dp_s[i - 1] + dp[i]) % mod
print(dp[n - 1])
