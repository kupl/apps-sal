class Solution:

    def distinctSubseqII(self, S: str) -> int:
        (dp, mod) = ([0] * len(S), 10 ** 9 + 7)
        for (i, char) in enumerate(S):
            ind = S.rfind(char, 0, i)
            dp[i] = 1 + sum(dp[:i]) % mod if ind == -1 else sum(dp[ind:i]) % mod
        return sum(dp) % mod
