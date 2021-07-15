import math
class Solution:
    
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False] * (n + 1)
        i = 1
        for i in range(1, n + 1):
            dp[i] = not all(dp[i - j*j] for j in range(1, int(math.sqrt(i)) + 1))
        print(dp)
        return dp[-1]
