class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False]*(n+1)
        dp[1] = True 
        for i in range(2, n+1):
            j = 1 
            while i - j**2 >= 0:
                if dp[i-j**2] is False:
                    dp[i] = True
                    break 
                j += 1 
            
        return dp[n]
