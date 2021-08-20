s = input()
n = len(s)
s += '0000000000'
dp = [[0] * 2 for i in range(n + 5)]
dp[n] = [1, 1]
res = set()
for i in range(n - 1, 4, -1):
    if i + 2 <= n and (dp[i + 2][0] and s[i:i + 2] != s[i + 2:i + 4] or dp[i + 2][1]):
        res.add(s[i:i + 2])
        dp[i][0] = 1
    if i + 3 <= n and (dp[i + 3][1] and s[i:i + 3] != s[i + 3:i + 6] or dp[i + 3][0]):
        res.add(s[i:i + 3])
        dp[i][1] = 1
print(len(res))
for ss in sorted(res):
    print(ss)
