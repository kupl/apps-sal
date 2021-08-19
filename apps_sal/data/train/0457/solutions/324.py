class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        self.dp = {}
        min_ = sys.maxsize
        for coin in coins:
            if amount - coin >= 0:
                min_ = min(min_, 1 + self.change(amount - coin, coins))
        if min_ == sys.maxsize:
            return -1
        return min_

    def change(self, amount, coins):
        if amount in self.dp:
            return self.dp[amount]
        if amount == 0:
            self.dp[amount] = 0
            return 0
        if amount in coins:
            self.dp[amount] = 1
            return 1
        min_ = sys.maxsize
        for coin in coins:
            if amount - coin >= 0:
                min_ = min(min_, 1 + self.change(amount - coin, coins))
        self.dp[amount] = min_
        return min_
