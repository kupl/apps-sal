class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] * (amount + 1)
        for i in range(1, amount + 1):
            minn = float('inf')
            for j in coins:
                if i == j:
                    minn = min(minn, 1)
                    continue
                if i - j > 0:
                    minn = min(minn, 1 + dp[i - j])
            dp[i] = minn
        return dp[amount] if dp[amount] != float('inf') else -1
