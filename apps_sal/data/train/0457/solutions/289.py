class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        self.memo = {0: 0}
        coins.sort()
        self.getMinCoins(coins, amount)
        if self.memo[amount] == float('inf'):
            return -1
        return self.memo[amount]

    def getMinCoins(self, coins, amount):
        if amount in self.memo:
            return self.memo[amount]
        minCoins = float('inf')
        for coin in coins:
            if amount - coin < 0:
                break
            currCoins = self.getMinCoins(coins, amount - coin) + 1
            minCoins = min(minCoins, currCoins)
        self.memo[amount] = minCoins
        return self.memo[amount]
