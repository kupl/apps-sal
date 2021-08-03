class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # i = coin index
        # c[i] = coin cost
        # f(0,0) = 0
        # f(coin, amount) = minimum number of coins needed to pay amount
        # f(i, j) = min( f(i-1, j), f(i, j-c[i]) + 1)

        dp = [amount + 1] * (amount + 1)

        dp[0] = 0

        for i in range(len(coins)):
            coin = coins[i]
            for j in range(1, amount + 1):
                sameCoin = amount + 1
                if j - coin >= 0:
                    dp[j] = min(dp[j - coin] + 1, dp[j])

        return dp[amount] if dp[amount] != amount + 1 else -1

#         rs = [amount+1] * (amount+1)
#         rs[0] = 0
#         for i in range(1, amount+1):
#             for c in coins:
#                 if i >= c:
#                     rs[i] = min(rs[i], rs[i-c] + 1)

#         if rs[amount] == amount+1:
#             return -1
#         return rs[amount]
