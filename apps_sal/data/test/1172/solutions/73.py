s = input()
MOD = 10 ** 9 + 7
dp = [1, 0, 0, 0]
for x in s:
    (emp, a, b, c) = dp
    if x == 'A':
        dp[1] += emp
    if x == 'B':
        dp[2] += a
    if x == 'C':
        dp[3] += b
    if x == '?':
        dp = [v * 3 for v in dp]
        dp[1] += emp
        dp[2] += a
        dp[3] += b
    dp = [v % MOD for v in dp]
print(dp[3])
