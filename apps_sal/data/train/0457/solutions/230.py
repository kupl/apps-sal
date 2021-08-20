class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount < 1:
            return 0
        self.cache = [0] * (amount + 1)
        return self.coin_change(coins, amount)

    def coin_change(self, coins, remainder):
        if remainder < 0:
            return -1
        if remainder == 0:
            return 0
        if self.cache[remainder] != 0:
            return self.cache[remainder]
        system_max = sys.maxsize
        minimum = system_max
        for coin in coins:
            change_result = self.coin_change(coins, remainder - coin)
            if change_result >= 0 and change_result < minimum:
                minimum = 1 + change_result
        self.cache[remainder] = -1 if minimum == system_max else minimum
        return self.cache[remainder]
