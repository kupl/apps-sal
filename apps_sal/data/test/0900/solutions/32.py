s = input()
ans, mod = [0] * 13, 10**9 + 7
if s[0] == "?":
    ans = [1] * 10 + [0] * 3
else:
    ans[int(s[0])] = 1
for i in s[1:]:
    dp = [0] * 13
    for j in range(13):
        dp[j * 10 % 13] = ans[j] % mod
    dp += dp
    if i == "?":
        for j in range(13):
            ans[j] = sum(dp[j + 4:j + 14])
    else:
        for j in range(13):
            ans[j] = dp[j + 13 - int(i)]
print(ans[5] % mod)
