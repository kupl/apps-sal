class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        # dp[i] if the player can win after i pile has been taken
        # dp[i] = one of dp[j1], dp[j2], is false ... where i - j_x is a square number
        
        dp = [False] * (n + 1)
        
        for i in reversed(range(n)):
            temp = 1
            while i + temp * temp <= n:
                j = i + temp * temp
                temp += 1
                if not dp[j]:
                    dp[i] = True
                    break
        
        return dp[0]
