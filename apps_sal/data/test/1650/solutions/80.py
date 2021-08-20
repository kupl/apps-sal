from pprint import pprint
MOD = 10 ** 9 + 7
L = input()
nl = len(L)
dp = [[0 for _ in range(2)] for _ in range(nl + 1)]
dp[0][0] = 1
for i in range(1, nl + 1):
    li = i - 1
    dp[i][1] = dp[i - 1][1] * 3 % MOD
    if L[li] == '1':
        dp[i][1] += dp[i - 1][0]
    if L[li] == '1':
        dp[i][0] = dp[i - 1][0] * 2 % MOD
    else:
        dp[i][0] = dp[i - 1][0]
    dp[i][0] %= MOD
    dp[i][1] %= MOD
print(sum(dp[-1]) % MOD)
