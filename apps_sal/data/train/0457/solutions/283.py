class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [0] * (amount+1)
        return self.dfs(coins, amount, memo)
    
    def dfs(self, coins: List[int], amount: int, memo: List[int]) -> int:
        if amount == 0:
            return 0
        
        if amount < 0:
            return -1
        
        if memo[amount] != 0:
            return memo[amount]
        
        minCoins = math.inf
        for coin in coins:
            res = self.dfs(coins, amount - coin, memo) + 1
            
            if res > 0:
                minCoins = min(minCoins, res)
        
        memo[amount] = minCoins if minCoins < math.inf else -1
        
        return minCoins if minCoins < math.inf else -1

