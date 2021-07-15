class Solution:
    def __init__(self):
        self.counts = {}
    
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount < 0:
            return -1
        if amount == 0:
            return 0
        if amount in self.counts:
            return self.counts[amount]
        minCoins = -1
        for val in coins:
            numCoins = self.coinChange(coins, amount - val)
            if numCoins != -1:
                if minCoins == -1:
                    minCoins = 1 + numCoins
                else:
                    minCoins = min(minCoins, 1+numCoins)
        self.counts[amount] = minCoins
        return minCoins
