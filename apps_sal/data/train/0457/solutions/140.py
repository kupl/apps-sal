class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return amount

        dp = [1e9 for _ in range(amount + 1)]
        dp[0] = 0

        for i in range(1, amount + 1):
            k = 1e9         # K = min num of coins to reach amount i
            for c in coins:
                if i - c >= 0:
                    k = min(k, dp[i - c] + 1)
            if k != 1e9:
                dp[i] = k

        return -1 if dp[amount] == 1e9 else dp[amount]
