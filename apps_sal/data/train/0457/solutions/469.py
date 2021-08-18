class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        self.dp = [float('inf')] * (amount + 1)
        self.dp[0] = 0

        def change(a):
            if a < 0:
                return -1
            if a == 0:
                return 0
            if self.dp[a] != float('inf'):
                return self.dp[a]
            for c in coins:
                tmp = change(a - c)
                if tmp != -1:
                    self.dp[a] = min(tmp + 1, self.dp[a])
            if self.dp[a] == float('inf'):
                self.dp[a] = -1
            return self.dp[a]

        change(amount)
        return self.dp[amount] if self.dp[amount] != float('inf') else -1
