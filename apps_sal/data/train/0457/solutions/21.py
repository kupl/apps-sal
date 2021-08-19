class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        numpath = [0] + [float('inf')] * amount
        for coin in coins:
            for i in range(coin, amount + 1):
                if numpath[i] > 1 + numpath[i - coin]:
                    numpath[i] = 1 + numpath[i - coin]
        return numpath[amount] if numpath[amount] != float('inf') else -1
