class Solution:

    def helper(self, amount: int) -> int:
        if amount in list(self.cache.keys()):
            return self.cache[amount]
        counts = []
        for coin in self.coins:
            if amount - coin > 0:
                counts.append(self.helper(amount - coin) + 1)
            elif amount - coin == 0:
                counts.append(1)
                break
        if counts == []:
            self.cache[amount] = 100000000
        else:
            self.cache[amount] = min(counts)
        return self.cache[amount]

    def coinChange(self, coins: List[int], amount: int) -> int:
        self.coins = coins
        if amount == 0:
            return 0
        self.cache = {}
        res = self.helper(amount)
        return res if res < 100000000 else -1
