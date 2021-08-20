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
            res = 1000
            for coin in coins:
                if dp(n - coin) == -1:
                    continue
                res = min(res, 1 + dp(n - coin))
            memo[n] = res if res != 1000 else -1
            return memo[n]
        return dp(amount)
