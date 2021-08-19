class Solution:

    def getLengthOfOptimalCompression(self, s: str, K: int) -> int:

        def getCost(k):
            if k <= 1:
                return k
            else:
                return 1 + len(str(k))
        n = len(s)
        dp = [[n] * (K + 1) for i in range(n + 1)]
        dp[0] = [0] * (K + 1)
        for i in range(n):
            for j in range(K + 1):
                if j > 0:
                    dp[i + 1][j - 1] = min(dp[i + 1][j - 1], dp[i][j])
                take = 0
                for k in range(i + 1)[::-1]:
                    if s[k] != s[i]:
                        take += 1
                    if take > j:
                        break
                    dp[i + 1][j - take] = min(dp[i + 1][j - take], dp[k][j] + getCost(i - k - take + 1))
        return min(dp[n])
