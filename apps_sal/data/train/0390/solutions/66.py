class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        sqrs = []
        for j in range(1, n + 1):
            if j * j <= n:
                sqrs.append(j * j)
            else:
                break
        dp = [False] * (1 + n)
        for s in sqrs: dp[s] = True
        
        for i in range(1, n + 1):
            if dp[i]: continue
            for s in sqrs:
                if s > i: break
                dp[i] = not dp[i - s]
                if dp[i]: break
        return dp[-1]
        

