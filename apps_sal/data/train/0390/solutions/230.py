class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        s = [i**2 for i in range(1, int(n**(1/2))+1)]
        dp = [0 for i in range(n+1)]
        dp[0], dp[1] = False, True
        
        for i in range(2, n+1):
            for j in s:
                if j > i:
                    dp[i] = False
                    break
                if dp[i-j] == False:
                    dp[i] = True
                    break
        
        return dp[-1]

