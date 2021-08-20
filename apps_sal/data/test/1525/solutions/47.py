(h, w, k) = map(int, input().split())
dp = [0] * w
l = [1, 1, 2, 3, 5, 8, 13, 21, 34]
dp[0] = 1
mod = 10 ** 9 + 7
r = [0] * w
for i in range(h):
    for i in range(w):
        r[i] = dp[i] * l[i] * l[w - 1 - i]
        if i >= 1:
            r[i] += dp[i - 1] * l[i - 1] * l[w - 1 - i]
        if i <= w - 2:
            r[i] += dp[i + 1] * l[i] * l[w - 2 - i]
        r[i] %= mod
    (dp, r) = (r, dp)
print(dp[k - 1])
