class Solution:

    def distinctSubseqII(self, S: str) -> int:
        (dp, MOD) = ([0] * len(S), 10 ** 9 + 7)
        for (i, char) in enumerate(S):
            ind = S.rfind(char, 0, i)
            dp[i] = 1 + sum(dp[:i]) % MOD if ind == -1 else sum(dp[ind:i]) % MOD
        return sum(dp) % MOD
