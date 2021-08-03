class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            curr_min = amount + 1
            for coin in coins:
                cand = amount + 1
                if i - coin >= 0:
                    cand = dp[i - coin] + 1
                if cand < curr_min:
                    curr_min = cand
            dp[i] = curr_min

        return -1 if dp[len(dp) - 1] == amount + 1 else dp[len(dp) - 1]
