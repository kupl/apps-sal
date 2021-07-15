class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [[float('inf')] * (amount + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = 0
        
        for i in range(1, n + 1):
            for j in range(1, amount + 1):
                dp[i][j] = min(dp[i-1][j], (dp[i][j-coins[i-1]] if j >= coins[i-1] else float('inf')) + 1)
        return dp[-1][-1] if dp[-1][-1] < float('inf') else -1
        # @lru_cache(None)
        # def dfs(amt, idx):
        #     # print(amt, idx)
        #     if idx < 0:
        #         if amt == 0:
        #             return 0
        #         else:
        #             return float('inf')
        #     if amt < 0:
        #         return float('inf')
        #     if amt == coins[idx]:
        #         return 1
        #     return min(dfs(amt - coins[idx], idx) + 1, dfs(amt, idx - 1))
        # res = dfs(amount, len(coins)-1)
        # return res if res < float('inf') else -1

