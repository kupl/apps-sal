class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = {}

        def recursion(S):
            if S == 0:
                return 0
            if S < 0:
                return float('inf')

            if S in dp:
                return dp[S]

            x = float('inf')
            for coin in coins:
                x = min(x, 1 + recursion(S - coin))

            dp[S] = x
            return x

        res = recursion(amount)
        if res == float('inf'):
            return -1

        return res
