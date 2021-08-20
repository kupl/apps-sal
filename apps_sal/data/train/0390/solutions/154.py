from math import sqrt


class Solution:

    def winnerSquareGame(self, n: int) -> bool:
        dp = [False] * (n + 1)
        dp[1] = True
        for m in range(2, n + 1):
            if sqrt(m) == int(sqrt(m)):
                dp[m] = True
                continue
            i = 1
            while i ** 2 < m:
                if not dp[m - i ** 2]:
                    dp[m] = True
                    break
                i += 1
        return dp[n]


"\nTrue,False, True, True, False, True, \nBrute force:\n\nBactracking method:\nproceed with removing a certain number of stones which are a square number\nand then have another state\n(stonesRemaining: int, AliceTurn: bool)\n\nso base case, if n == 0 or person can't make any moves: return not AliceTurn\n\nconstruct dp table of two dimensions \n\nat any subproblem m, if alice wins, then bob necessarily loses and vice versa \n\nn =1 \nn is a square, return True\n\nn= 2, \nn is not square so only option is take 1 stone\n(2) -> (1) -> False\n\nn= 4\nif n is a square: return True\n\nn = 7 \ndp(1) : return True meaning alice wins\ndp(n: int) -> bool :\n    if sqrt(n) == int(sqrt(n)) : return True\n    i = 1\n    while i**2 < n : \n        if dp[n-i] : return True\n        i +=1 \n    return True\n\nreturn not dp(n)\n\n"
