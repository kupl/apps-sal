class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # initialize a dp table for the minimum amount of coins needed
        # to get each value up to the amount (all except 0 are inf)
        dp = [0] + [float('inf')] * amount

        # then for i up to the amount and counting each coin
        for i in range(1, amount + 1):
            for c in coins:
                # if you can subtract the coin from the current amount
                # get new min (current or with the new coin)
                if i - c >= 0:
                    # dp[i-c] + 1: minimum of the amount subtracting the coin
                    # we are at now if we added this 1 coin
                    dp[i] = min(dp[i], dp[i - c] + 1)

        if dp[-1] == float('inf'):
            return -1
        return dp[-1]
