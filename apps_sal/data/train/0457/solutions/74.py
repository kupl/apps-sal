class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #         方法一: dp[i] = min(dp[i],dp[amount-i]+1)
        # dp = [0]
        # length = len(coins)
        # for i in range(1, amount+1):
        #     dp += [9999]
        #     for j in range(length):
        #         if i >= coins[j] and dp[int(i-coins[j])] != 9999:
        #             dp[i] = min(dp[i], dp[int(i-coins[j])] + 1)
        # if dp[amount] == 9999:
        #     return -1
        # return dp[amount]

        #         优化后的方法: dp[x+c] = min(dp[x]+1, dp[x+c])
        dp = [0] + [-1] * amount
        for x in range(amount + 1):
            if dp[x] < 0:
                continue
            for c in coins:
                if x + c > amount:
                    continue
                if dp[x + c] < 0 or dp[x + c] > dp[x] + 1:
                    dp[x + c] = dp[x] + 1
        return dp[amount]

        # dp = [0] + [-1] * amount
        # for x in range(amount):
        #     if dp[x] < 0:
        #         continue
        #     for c in coins:
        #         if x + c > amount:
        #             continue
        #         if dp[x + c] < 0 or dp[x + c] > dp[x] + 1:
        #             dp[x + c] = dp[x] + 1
        # return dp[amount]
