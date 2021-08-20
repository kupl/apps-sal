class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        dp = [amount] * (amount + 1)
        dp[0] = 0
        pos = 1
        contain = False
        while pos < len(dp):
            for coin in coins:
                if coin == 1:
                    contain = True
                if pos - coin >= 0:
                    dp[pos] = min(dp[pos], dp[pos - coin] + 1)
            pos += 1
        print(dp)
        if dp[-1] == amount and (not contain):
            return -1
        return dp[-1]
