class Solution:

    def distinctSubseqII(self, S: str) -> int:
        MOD = 10 ** 9 + 7
        n = len(S)
        dp = collections.Counter()
        result = 0
        for i in range(n - 1, -1, -1):
            old = result
            result = (2 * old + 1 - dp[S[i]]) % MOD
            dp[S[i]] += result - old
        return result
