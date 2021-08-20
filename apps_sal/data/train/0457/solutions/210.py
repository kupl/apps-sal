class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        self.coins = coins
        self.amount = amount
        self.cache = {}
        res = self.getValue(self.amount)
        if res is None:
            return -1
        else:
            return res

    def getValue(self, amount):
        if amount in self.cache:
            return self.cache[amount]
        if amount < 0:
            return None
        if amount == 0:
            return 0
        if amount in self.coins:
            return 1
        min_count = None
        for coin in self.coins:
            count = self.getValue(amount - coin)
            if count is not None:
                if min_count is None or min_count > count + 1:
                    min_count = count + 1
        self.cache[amount] = min_count
        return min_count
