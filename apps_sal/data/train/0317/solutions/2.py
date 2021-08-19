class Solution:
    def numPermsDISequence(self, S: str) -> int:
        n = len(S) + 1
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        dp[1][0] = 1
        MOD = 10**9 + 7
        for i in range(2, n + 1):
            p = [0] + list(itertools.accumulate(dp[i - 1]))

            for j in range(i):
                L, R = None, None
                if S[i - 2] == 'D':  # decreasing
                    L = j
                    R = i - 2

                else:  # increasing
                    L = 0
                    R = j - 1

                dp[i][j] = (p[R + 1] - p[L]) % MOD
                dp[i][j] %= MOD

        res = 0
        for i in dp[n]:
            res += i
            res %= MOD
        return res
