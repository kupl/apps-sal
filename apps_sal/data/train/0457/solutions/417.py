class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [sys.maxsize] * amount

        for i in range(1, amount + 1):
            for coin in sorted(coins):
                if i < coin:
                    break
                dp[i] = min(dp[i], dp[i - coin] + 1)

        return -1 if dp[-1] == sys.maxsize else dp[-1]
