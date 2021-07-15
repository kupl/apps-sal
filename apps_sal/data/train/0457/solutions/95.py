from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount:
            return 0
        solution = -1
        dp = [0] * (amount + 1)
        for i in range(1, amount + 1):
            dp[i] = min([dp[i - coin] for coin in coins if i - coin >= 0] + [10000]) + 1

        if dp[-1] != 10001:
            solution = dp[-1]
        return solution
