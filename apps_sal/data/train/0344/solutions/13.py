class Solution:
    def minDeletionSize(self, a: List[str]) -> int:
        n, m = len(a), len(a[0])
        dp = [1 for i in range(m)]
        # dp[0] = 1
        maxx = 1
        for i in range(1, m):
            for j in range(i):
                if all(a[k][i] >= a[k][j] for k in range(n)):
                    dp[i] = max(dp[i], dp[j] + 1)
                    maxx = max(maxx, dp[i])
        return m - maxx
