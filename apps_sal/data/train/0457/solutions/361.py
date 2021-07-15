class Solution:
    cache = {}
    def coinChange(self, coins: List[int], amount: int) -> int:
        self.cache = {}
        return self.solve(coins, amount)

    def solve(self, coins, amount):
        if amount == 0:
            return 0
        if amount < 0:
            return -1

        if amount in self.cache:
            return self.cache[amount]

        best = -1
        for c in coins:
            add = self.solve(coins, amount - c)
            if add != -1:
                if best == -1:
                    best = add + 1
                else:
                    best = min(best, add + 1)

        self.cache[amount] = best
        return best
