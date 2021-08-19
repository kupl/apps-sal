class Solution:

    def distinctSubseqII(self, S: str) -> int:
        mod = 10 ** 9 + 7
        n = len(S)
        dp = [0] * n
        dp[0] = 1
        for i in range(1, n):
            dp[i] = dp[i - 1] * 2 + 1
            for j in range(i - 1, -1, -1):
                if S[j] == S[i]:
                    if j > 0:
                        dp[i] -= dp[j - 1]
                    dp[i] -= 1
                    break
            dp[i] %= mod
        return dp[-1]
