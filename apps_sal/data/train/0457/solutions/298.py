class Solution(object):

    def __init__(self):
        self.mem = {0: 0}

    def getMinCoins(self, coins, amount):
        if amount in self.mem:
            return self.mem[amount]
        minCoins = float('inf')
        for c in coins:
            if amount - c < 0:
                break
            numCoins = self.getMinCoins(coins, amount - c) + 1
            minCoins = min(numCoins, minCoins)
        self.mem[amount] = minCoins
        return minCoins

    def coinChange(self, coins, amount):
        minCoins = self.getMinCoins(sorted(coins), amount)
        if minCoins == float('inf'):
            return -1
        return minCoins
