class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1] * (amount + 1)
        dp[0] = 0
        for idx in range(amount + 1):
            tmp = []
            for coin in coins:
                if idx - coin >= 0 and dp[idx - coin] != -1:
                    tmp.append(dp[idx - coin])
            if tmp:
                dp[idx] = min(tmp) + 1
        print(dp)
        return dp[-1]
