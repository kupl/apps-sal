class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount:
            return 0
        coins.sort()
        self.coins = coins
        self.memo = {}
        self.recursion(amount)
        return -1 if self.memo[amount] == float('inf') else self.memo[amount]

    def recursion(self, amt):
        min_coins = float('inf')
        if amt == 0:
            return 0
        if amt in self.memo:
            return self.memo[amt]
        for coin in self.coins:
            if coin > amt:
                break
            x = self.recursion(amt - coin)
            min_coins = min(min_coins, x)
        self.memo[amt] = 1 + min_coins
        return self.memo[amt]
