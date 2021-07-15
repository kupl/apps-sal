class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        '''
        dp = [False] * (n + 1)
        for i in range(1, n+1):
            for k in range(1, i+1):
                if i - k**2 < 0: break
                if not dp[i - k**2]: dp[i] = True;break
            #print(dp)        
        return dp[-1]
        '''
        dp = [False] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = not all(dp[i - k * k] for k in range(1, int(i**0.5) + 1))
        return dp[-1]   
