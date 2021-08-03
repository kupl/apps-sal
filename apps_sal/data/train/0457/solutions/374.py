class Solution:
    memory = {}

    def numCoins(self, coins, amount):
        if amount in self.memory:
            return self.memory[amount]

        nc = float('inf')
        for c in coins:
            if amount >= c:
                nnc = self.numCoins(coins, amount - c)
                nc = min(nc, nnc + 1)

        self.memory[amount] = nc
        return nc

    def coinChange(self, coins: List[int], amount: int) -> int:
        self.memory = {}
        self.memory[0] = 0
        for c in coins:
            self.memory[c] = 1

        nc = self.numCoins(coins, amount)
        if nc == float('inf'):
            return -1

        return nc
