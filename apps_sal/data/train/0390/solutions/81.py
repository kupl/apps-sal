class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        
        def dp_search(dp, n):
            if n == 0:
                return False
            if n == 1:
                return True
            
            if n in dp:
                return dp[n]
            
            dp[n] = False
            i = int(sqrt(n))
            while i>=1:
                if dp_search(dp, n-i*i)==False:
                    dp[n] = True
                    return True
                i-=1
            
            return False
        
        
        dp = {}
        return dp_search(dp, n)

