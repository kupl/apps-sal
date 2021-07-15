class Solution:
    def numPermsDISequence(self, S: str) -> int:
        n = len(S)
        MOD = 10 ** 9 + 7

        dp = [[0]*(n+1) for _ in range(n+1)]

        dp[0][0] = 1

        for i in range(1, n+1):
            for j in range(i+1):
                if S[i-1] == 'D':
                    dp[i][j] = sum(dp[i-1][j:i] + [0]) % MOD
                else:
                    dp[i][j] = sum(dp[i-1][:j] + [0]) % MOD
        return sum(dp[-1]) % MOD
