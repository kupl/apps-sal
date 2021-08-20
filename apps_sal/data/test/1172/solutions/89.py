MOD = 10 ** 9 + 7
S = input()
dp = []
for i in range(len(S) + 1):
    dp.append([0, 0, 0, 0])
dp[-1][3] = 1
for i in reversed(range(len(S))):
    if S[i] == '?':
        m1 = 3
    else:
        m1 = 1
    dp[i][3] = m1 * dp[i + 1][3]
    dp[i][3] %= MOD
    for j in range(3):
        if S[i] == '?':
            m2 = 1
        elif S[i] == ['A', 'B', 'C'][j]:
            m2 = 1
        else:
            m2 = 0
        dp[i][j] = m1 * dp[i + 1][j] + m2 * dp[i + 1][j + 1]
        dp[i][j] %= MOD
print(dp[0][0])
