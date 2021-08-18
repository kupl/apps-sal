class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = [0] * (amount + 1)
        for ind in range(1, amount + 1):
            min_coins = float('inf')

            for coin in coins:
                if ind - coin >= 0:
                    coins_needed = cache[ind - coin] + 1
                    if coins_needed < min_coins:
                        min_coins = coins_needed
            cache[ind] = min_coins
        if cache[amount] == float('inf'):
            return -1
        return cache[amount]
