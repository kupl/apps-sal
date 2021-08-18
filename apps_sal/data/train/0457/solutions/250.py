class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount:
            return 0
        dp: List[int] = [0 for _ in range(amount)]

        for i in range(amount):
            for coin in coins:
                if coin > i + 1:
                    continue
                if coin == i + 1:
                    dp[i] = 1
                elif dp[i - coin] != 0:
                    if dp[i] == 0:
                        dp[i] = dp[i - coin] + 1
                    else:
                        dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[amount - 1] if dp[amount - 1] != 0 else -1
