import math


class Solution:
    trellis = None

    def coinChange(self, coins: List[int], amount: int) -> int:
        if self.trellis == None:
            self.trellis = [math.inf] * (amount + 1)
            self.trellis[0] = 0
        if self.trellis[amount] != math.inf:
            return self.trellis[amount]
        if amount < 0:
            return -1
        minVal = math.inf
        for coin in coins:
            required = amount - coin
            if required < 0:
                continue
            val = self.trellis[required] if self.trellis[required] != math.inf else self.coinChange(coins, required)
            if val == -1:
                continue
            else:
                minVal = min(minVal, val + 1)
        if minVal == math.inf:
            minVal = -1
        self.trellis[amount] = min(self.trellis[amount], minVal)
        return minVal
