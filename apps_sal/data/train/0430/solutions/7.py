class Solution:

    def distinctSubseqII(self, S: str) -> int:
        mod = 1000000007
        if not S:
            return 0
        d = {}
        dp = [0 for i in range(0, len(S))]
        dp[0] = 2
        d[S[0]] = 0
        for i in range(1, len(S)):
            dp[i] = 2 * dp[i - 1]
            v = 0
            if S[i] in d:
                last = d[S[i]]
                if last - 1 >= 0:
                    v = dp[last - 1]
                else:
                    v = 1
            dp[i] = (dp[i] - v) % mod
            d[S[i]] = i
        return dp[-1] - 1
