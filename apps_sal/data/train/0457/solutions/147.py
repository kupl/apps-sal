import math


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        count = [math.inf] * (amount + 1)
        count[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if i >= coin:
                    count[i] = min(count[i], count[i - coin] + 1)

        return count[amount] if count[amount] != math.inf else -1
