class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def helper(coins, amount, n, t):
            if n == 0:
                return float('inf')
            if amount == 0:
                return 0
            if n == 1 and amount % coins[n - 1] == 0:
                return amount // coins[n - 1]
            if t[n][amount] == -1:
                if coins[n - 1] <= amount:
                    t[n][amount] = min(1 + helper(coins, amount - coins[n - 1], n, t), helper(coins, amount, n - 1, t))
                else:
                    t[n][amount] = helper(coins, amount, n - 1, t)
            return t[n][amount]

        n = len(coins)
        t = [[-1 for j in range(amount + 1)] for i in range(n + 1)]
        minCoins = helper(coins, amount, n, t)
        if minCoins == float('inf'):
            return -1
        else:
            return minCoins
