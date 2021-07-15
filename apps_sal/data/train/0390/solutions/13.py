class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        # W(a) = n - W(b) if W(a) is a square number
        # dp[i]: for n = i, if first one can win or not
        # if there's a \"k\" that can make dp[i - k*k] == False, then the other guy lose, and by making dp[i] = True
        dp = [False]*(n+1)
        for i in range(1, n+1):
            k = 1
            while k*k <= i:
                if dp[i-k*k] == False:
                    dp[i] = True
                    break
                k += 1
        return dp[n]
