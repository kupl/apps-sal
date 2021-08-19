class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}

        def dfs(total):
            if total < 0:
                return float('inf')
            if total == 0:
                return 0
            if total in list(dp.keys()):
                return dp[total]
            for c in coins:
                x = total - c
                if total not in list(dp.keys()):
                    dp[total] = dfs(x) + 1
                else:
                    dp[total] = min(dp[total], dfs(x) + 1)
            return dp[total]
        ans = dfs(amount)
        if ans < float('inf'):
            return ans
        else:
            return -1
