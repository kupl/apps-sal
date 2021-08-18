import numpy as np


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = np.empty(amount + 1)
        dp.fill(math.inf)
        dp[0] = 0

        coins = sorted(coins)

        for i in range(1, amount + 1):
            for c in coins:
                if c <= i:
                    dp[i] = min(dp[i], 1 + dp[i - c])
                else:
                    break
        return -1 if dp[-1] == math.inf else int(dp[-1])
