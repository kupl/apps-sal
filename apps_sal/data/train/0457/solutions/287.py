class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [None for _ in range(amount + 1)]

        def fewest_num(amount, dp):
            if dp[amount] is not None:
                return dp[amount]
            if amount == 0:
                min_num = 0
            elif amount < min(coins):
                min_num = float('inf')
            elif amount in set(coins):
                min_num = 1
            else:
                min_num = float('inf')
                for coin in coins:
                    if amount - coin >= 0:
                        num = fewest_num(amount - coin, dp)
                        min_num = min(min_num, num)
                min_num += 1

            dp[amount] = min_num
            return min_num

        min_num = fewest_num(amount, dp)
        if min_num == float('inf'):
            return -1
        return min_num
