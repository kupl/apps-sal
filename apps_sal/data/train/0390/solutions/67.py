class Solution:

    def winnerSquareGame(self, n: int) -> bool:
        dp = [False] * (n + 1)
        dp[1] = True
        for i in range(2, n + 1):
            j = 1
            flag = False
            while j * j <= i:
                if not dp[i - j * j]:
                    flag = True
                    break
                j += 1
            dp[i] = flag
        return dp[-1]
