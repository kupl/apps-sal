class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [-1] * amount
        for i in range(len(dp)):
            if dp[i] < 0:
                continue
            for x in coins:
                if i + x > amount:
                    continue
                if dp[i + x] == -1 or dp[i + x] > dp[i] + 1:
                    dp[i + x] = dp[i] + 1
        return dp[-1]
