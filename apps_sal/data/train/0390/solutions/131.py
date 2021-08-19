class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        # time O(n*sqrt(n)), space O(n)
        dp = [False] * (n + 1)  # dp[i] means Alice can win with i
        dp[1] = True
        for i in range(2, n + 1):
            for k in range(1, int(i**0.5) + 1):
                if dp[i - k * k] == False:  # if Bob can't win, then Alice wins
                    dp[i] = True
        return dp[n]
