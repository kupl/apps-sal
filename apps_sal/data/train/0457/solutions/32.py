from collections import defaultdict


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        MAX = float('inf')
        dp = defaultdict(lambda: MAX)
        dp[0] = 0
        for i in range(1, amount + 1):
            dp[i] = 1 + min([dp[i - c] for c in coins])
        return -1 if dp[amount] == MAX else dp[amount]
