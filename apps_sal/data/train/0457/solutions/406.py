class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [[math.inf for i in range(amount + 1)] for i in range(len(coins))]
        for i in range(len(coins)):
            dp[i][0] = 0
        for i in range(len(coins)):
            for j in range(amount + 1):
                if i > 0:
                    dp[i][j] = dp[i - 1][j]
                if j >= coins[i]:
                    dp[i][j] = min(dp[i][j], dp[i][j - coins[i]] + 1)
        return -1 if dp[-1][-1] == math.inf else dp[-1][-1]
        
    

