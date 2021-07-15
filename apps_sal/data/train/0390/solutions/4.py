class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False] * (max(n, 2)+1)
        dp[0] = False
        dp[1] = True
        dp[2] = False
        #dp[3] = True
        #dp[4] = 

        squares = [i**2 for i in range(1, floor(sqrt(n))+1)]
        
        for i in range(3, n+1):
            for square in squares:
                if i - square < 0:
                    break
                if dp[i - square] == False:
                    dp[i] = True
                    break
        #print(dp)
        return dp[n]

