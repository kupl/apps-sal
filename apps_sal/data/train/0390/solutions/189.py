class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [-1 for i in range(n+1)]
        
        def help(n):
            if dp[n]==-1:            
                if n<1:
                    result = False
                else:
                    result = False
                    i=1
                    while i**2 <= n:
                        move = i**2
                        result = result or not(help(n-move))
                        if result:
                            break
                        i+=1
                        
                dp[n] = result
            return dp[n]
        return help(n)
