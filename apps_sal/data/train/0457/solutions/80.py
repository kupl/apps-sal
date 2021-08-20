class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(min(coins), amount + 1):
            tmp = list()
            for coin in coins:
                if i - coin < 0:
                    tmp.append(float('inf'))
                else:
                    tmp.append(dp[i - coin])
            dp[i] = min(tmp) + 1
        return dp[-1] if dp[-1] != float('inf') else -1
