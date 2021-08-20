class Solution:

    def coinChange(self, coin: List[int], amount: int) -> int:
        dp = [[9999999 for _ in range(amount + 1)] for _ in range(len(coin) + 1)]
        for i in range(1, len(coin) + 1):
            dp[i][0] = 0
        for i in range(1, len(coin) + 1):
            for j in range(1, amount + 1):
                if j >= coin[i - 1]:
                    dp[i][j] = min(dp[i][j - coin[i - 1]] + 1, dp[i - 1][j])
                else:
                    dp[i][j] = dp[i - 1][j]
        if dp[-1][-1] == 9999999:
            return -1
        return dp[-1][-1]
