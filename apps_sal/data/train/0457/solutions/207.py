class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [sys.maxsize] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for c in coins:
                if 0 <= i - c < amount + 1:
                    dp[i] = min(dp[i], dp[i - c] + 1)
        return dp[-1] if dp[-1] != sys.maxsize else -1
