class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf') for _ in range(amount + 1)]

        if(amount == 0):
            return 0

        for i in range(0, len(dp)):
            for c in coins:
                if(i >= c):
                    if(i % c == 0):
                        dp[i] = min(int(i / c), dp[i])
                    else:
                        if(i - c >= 0 and dp[i - c] != float('inf')):
                            dp[i] = min(int(1 + dp[i - c]), dp[i])

        ret_val = dp[amount]
        if(ret_val == float('inf')):
            return -1
        return dp[amount]
