class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        self.smallest = float('inf')
        coins.sort(reverse=True)
        self.dfs(coins, amount, 0)
        return -1 if type(self.smallest) is float else self.smallest

    def dfs(self, coins, amount, prev_count):
        if len(coins) == 0:
            return
        if amount % coins[0] == 0:
            self.smallest = min(self.smallest, prev_count + amount // coins[0])
        else:
            for k in range(amount // coins[0], -1, -1):
                if prev_count + k >= self.smallest:
                    break
                self.dfs(coins[1:], amount - k * coins[0], prev_count + k)
