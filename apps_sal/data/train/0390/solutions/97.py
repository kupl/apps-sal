import math
class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False for _ in range(n+1)] # init dp[0] as False since it implies no move to make.
        dp[1] = True # known corner case
        for i in range(2,n+1): # for every i in [2,n]
            sqr = int(i**0.5) # calculate upper bound for integer square root less than i
            for j in range(1, sqr+1): # for every integer square root less than sqrt(i)
                dp[i] |= not dp[i-j**2] # if there is any n == (i-j**2) that is doomed to lose, i should be true.
                                        # because Alice can make that move(remove j**2 stones) and make Bob lose.
                                        # otherwise i should be false since there is no any choice that will lead to winning.
                if dp[i]: # Optimization due to test case TLE: if it is already true, break out.
                    break
        return dp[n]
                
                
                
        
        

