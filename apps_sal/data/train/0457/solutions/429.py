class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = dict()

        def dp(n):
            if n in memo:
                return memo[n]
            if n == 0:
                return 0
            if n < 0:
                return -1
            res = float('inf')
            for coin in coins:
                sub = dp(n - coin)
                if sub == -1:
                    continue
                res = min(res, dp(n - coin) + 1)
            memo[n] = res if res != float('inf') else -1
            return memo[n]
        return dp(amount)
