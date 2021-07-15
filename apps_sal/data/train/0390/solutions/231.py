class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False] * (n + 1)
        for i in range(1, n + 1):
            for base in range(1, int(math.sqrt(i)) + 1):
                take = base * base
                if not dp[i - take]:
                    dp[i] = True
                    break
        return dp[n]
