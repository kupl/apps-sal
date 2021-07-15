class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        self.dp = [[-1]*(amount+1) for _ in range(len(coins) + 1)]
        value = self.solve(coins, len(coins), amount)
        return self.dp[-1][-1] if value != float('inf') else -1

    
    def solve(self, coins, n, amount):
        if amount == 0:
            self.dp[n][amount] = 0
            return 0
        if n == 0:
            self.dp[n][amount] = float('inf')
            return self.dp[n][amount]
        if self.dp[n][amount] != -1:
            return self.dp[n][amount]
        if coins[n-1] <= amount:
            self.dp[n][amount] =  min(1 + self.solve(coins, n, amount - coins[n-1]), self.solve(coins, n-1, amount))
            return self.dp[n][amount]
        else:
            self.dp[n][amount] = self.solve(coins, n-1, amount)
            return self.dp[n][amount]
