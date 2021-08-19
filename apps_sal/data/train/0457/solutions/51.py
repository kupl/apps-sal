class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        min_coins = [float('inf') for x in range(amount + 1)]
        min_coins[0] = 0
        for value in range(1, amount + 1):
            for coin in coins:
                if coin <= value:
                    if min_coins[value - coin] + 1 < min_coins[value]:
                        min_coins[value] = min_coins[value - coin] + 1
        if min_coins[amount] == float('inf'):
            return -1
        return min_coins[amount]
