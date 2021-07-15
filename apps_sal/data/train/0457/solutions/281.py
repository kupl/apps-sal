class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        def helper(coins, amount, dp):
            if amount < 0:
                return float('inf')
            if amount == 0:
                return 0
            if amount in dp:
                return dp[amount]
            ans = []
            for i in range(len(coins)):
                use_ci = 1 + helper(coins, amount - coins[i], dp)
                ans.append(use_ci)
                
            dp[amount] = min(ans)
 
            return dp[amount]
        
        if amount <= 0:
            return 0
        dp = {}
        result = helper(coins, amount, dp)
        return -1 if result == float('inf') else result
    


