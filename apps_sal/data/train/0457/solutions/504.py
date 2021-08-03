class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)

        count = 0
        self.maxcount = float('inf')

        self.dfs(coins, count, amount)

        return -1 if self.maxcount == float('inf') else self.maxcount

    def dfs(self, coins, count, amount):
        if amount == 0:
            self.maxcount = min(self.maxcount, count)

        for i in range(len(coins)):
            if amount >= coins[i] and count + math.ceil(amount / coins[i]) < self.maxcount:
                self.dfs(coins[i:], count + 1, amount - coins[i])
