def solve(S):
    N = len(S)
    MOD = 1000000007
    dp = [0] * 13
    dp[0] = 1
    for i in range(N):
        tmp = [0] * 13
        c = -1 if S[i] == '?' else int(S[i])
        for j in range(10):
            if c != -1 and c != j:
                continue
            for k in range(13):
                tmp[(j + k * 10) % 13] += dp[k]
        for j in range(13):
            dp[j] = tmp[j] % MOD
    return dp[5]


print(solve(input()))
