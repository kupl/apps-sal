class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [float('inf') for _ in range(amount+1)]
        memo[0] = 0
        for c in coins:
            for i in range(c, len(memo)):
                memo[i] = min(1 + memo[i-c], memo[i])
        
        return memo[amount] if memo[amount] != float('inf') else -1
