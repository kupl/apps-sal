class Solution:
    def minDays(self, n: int) -> int:

        dp = dict()

        def dfs(n, l):
            if l > 100:
                return sys.maxsize

            if n in dp:
                return dp[n]

            if n == 1:
                dp[n] = 1
                return dp[n]

            dp[n] = sys.maxsize

            if n % 3 == 0:
                dp[n] = min(dp[n], dfs(n // 3, l + 1) + 1)

            if n % 2 == 0:
                dp[n] = min(dp[n], dfs(n // 2, l + 1) + 1)

            dp[n] = min(dp[n], dfs(n - 1, l + 1) + 1)

            return dp[n]

        return dfs(n, 0)
