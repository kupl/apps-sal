from math import sqrt


class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False] * (n + 1)
        dp[1] = True

        for m in range(2, n + 1):

            i = 1
            while i**2 < m:
                if not dp[m - i**2]:

                    dp[m] = True
                    break
                i += 1
            if i**2 == m:
                dp[m] = True

        return dp[n]


'''
True,False, True, True, False, True, 
Brute force:

Bactracking method:
proceed with removing a certain number of stones which are a square number
and then have another state
(stonesRemaining: int, AliceTurn: bool)

so base case, if n == 0 or person can't make any moves: return not AliceTurn

construct dp table of two dimensions 

at any subproblem m, if alice wins, then bob necessarily loses and vice versa 

n =1 
n is a square, return True

n= 2, 
n is not square so only option is take 1 stone
(2) -> (1) -> False

n= 4
if n is a square: return True

n = 7 
dp(1) : return True meaning alice wins
dp(n: int) -> bool :
    if sqrt(n) == int(sqrt(n)) : return True
    i = 1
    while i**2 < n : 
        if dp[n-i] : return True
        i +=1 
    return True

return not dp(n)

'''
