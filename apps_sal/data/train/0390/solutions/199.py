class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [0,1]
        
        for s in range(2,n+1):
            dp.append(0)
            i = 1
            while i**2 <= s:
                dp[-1] = max(dp[-1], 1-dp[s-i**2])
                if dp[-1] == 1: break
                i += 1
        return dp[-1]
