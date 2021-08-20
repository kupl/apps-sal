class Solution:

    def winnerSquareGame(self, n: int) -> bool:
        dp = defaultdict(bool)

        def helper(n):
            if n == 0:
                return False
            if n in dp:
                return dp[n]
            for i in range(1, int(n ** 0.5) + 1):
                if not helper(n - i ** 2):
                    dp[n] = True
                    return True
            dp[n] = False
            return False
        return helper(n)
