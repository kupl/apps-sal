MOD = 1000000007

s = [-1 if x == '?' else int(x) for x in input()]
n = len(s) + 1

dp = [0] * 13
dp[0] = 1

r = [[(j - i) * 4 % 13 for i in range(10)]for j in range(13)]

for i, x in enumerate(s):
    next_dp = [0] * 13
    if x == -1:
        next_dp = [sum(dp[i] for i in j) for j in r]
    else:
        next_dp = [dp[j[x]] for j in r]
    dp = [k % MOD for k in next_dp]

print(dp[5])
