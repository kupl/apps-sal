class Solution:
    def __init__(self):
        self.cache = dict()
        self.coin_set = set()

    def helper(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        if amount in self.cache:
            return self.cache[amount]
        if amount in self.coin_set:
            return 1
        potentials = [float('inf')]
        for coin in coins:
            if amount > coin:
                potentials.append(self.helper(coins, amount - coin))
        res = 1 + min(potentials)
        self.cache[amount] = res
        return res

    def coinChange(self, coins: List[int], amount: int) -> int:
        self.coin_set = set(coins)
        coins = sorted(coins, reverse=True)
        res = self.helper(coins, amount)
        if res == float('inf'):
            return -1
        return res
