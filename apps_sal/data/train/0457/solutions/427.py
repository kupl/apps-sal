class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        sz = len(coins) + 1
        dp = [[sys.maxsize] * sz for _ in range(amount + 1)]
        for i in range(sz):
            dp[0][i] = 0
        for a in range(1, amount + 1):
            for i in range(1, sz):
                dp[a][i] = dp[a][i - 1]
                if a - coins[i - 1] >= 0:
                    dp[a][i] = min(1 + dp[a - coins[i - 1]][i], dp[a][i])
        return -1 if dp[amount][sz - 1] == sys.maxsize else dp[amount][sz - 1]
