class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coin_count = len(coins)
        
        dp = [[math.inf for i in range(coin_count + 1)] for j in range(amount + 1)]
        for i in range(coin_count + 1):
            dp[0][i] = 0 
        for i in range(1, amount + 1):
            for j in range(1, coin_count + 1):
                if coins[j - 1] <= i:
                    dp[i][j] = min(1 + dp[i - coins[j - 1]][j], dp[i][j - 1])
                else:
                    dp[i][j] = dp[i][j - 1]
        if dp[-1][-1] == math.inf: return -1
        return dp[-1][-1]
