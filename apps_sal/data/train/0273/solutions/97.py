class Solution:

    def racecar(self, target: int) -> int:

        def dfs(t):
            if t in dp:
                return dp[t]
            n = t.bit_length()
            if 2 ** n - 1 == t:
                dp[t] = n
            else:
                dp[t] = dfs(2 ** n - 1 - t) + n + 1
                for m in range(n - 1):
                    dp[t] = min(dp[t], dfs(t - 2 ** (n - 1) + 2 ** m) + n + m + 1)
            return dp[t]
        dp = {0: 0}
        return dfs(target)
