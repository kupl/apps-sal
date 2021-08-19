class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        self.amount = amount
        self.coins = coins
        n = len(coins)
        self.memo = [-1] * (self.amount + 1)
        val = self.coindp(amount)
        if val == float('inf'):
            return -1
        else:
            return val

    def coindp(self, i):
        if i < 0:
            return float('inf')
        if i == 0:
            return 0

        if self.memo[i] >= 0:
            return self.memo[i]

        mini = float('inf')
        for coin in self.coins:
            mini = min(mini, self.coindp(i - coin) + 1)

        self.memo[i] = mini
        # print(self.memo)
        return self.memo[i]
