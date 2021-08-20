from collections import deque


class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        dp = [float('inf')] * (amount + 1)
        dp[amount] = 0
        queue = deque()
        queue.append(amount)
        while len(queue) != 0:
            val = queue.popleft()
            for coin in coins:
                if val - coin == 0:
                    return dp[val] + 1
                if val - coin > 0:
                    if dp[val] + 1 < dp[val - coin]:
                        dp[val - coin] = dp[val] + 1
                        queue.append(val - coin)
        return -1
