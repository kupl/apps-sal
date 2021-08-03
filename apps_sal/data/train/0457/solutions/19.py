class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        INVALID = float('inf')
        dp = [INVALID] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for i in range(coin, amount + 1):
                if dp[i - coin] >= dp[i]:
                    continue
                dp[i] = dp[i - coin] + 1
        return -1 if dp[amount] == INVALID else dp[amount]

        # # sol 2 dp bottom up
        # INVALID = float('inf')
        # dp = [INVALID] * (amount + 1)
        # dp[0] = 0
        # for i in range(amount + 1):
        #     for coin in coins:
        #         remains = i - coin
        #         if remains < 0: continue
        #         dp[i] = min(dp[i], dp[remains] + 1)
        # return -1 if dp[amount] == INVALID else dp[amount]

        # # sol 1 dp with memo
        # memo = {}
        # def dp(n):
        #     if n in memo: return memo[n]
        #     if n < 0: return -1
        #     if n == 0: return 0
        #     res = float('inf')
        #     for coin in coins:
        #         sub = dp(n - coin)
        #         if sub == -1: continue
        #         res = min(res, 1 + sub)
        #     memo[n] = res if res != float('inf') else -1
        #     return memo[n]
        # return dp(amount)
