import math
class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False for i in range(n+1)]
        dp[0] = True
        dp[1] = True
        for i in range(3, n+1):
            if math.sqrt(i) == int(math.sqrt(i)):
                dp[i] = True
                continue
            start = 1
            while(start*start < i):
                if not dp[i-start*start]:
                    dp[i] = True
                    break
                start += 1
        print(dp)
        return dp[n]
