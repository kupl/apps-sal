class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False]
        for i in range(1, n + 1):
            b = 1
            winnable = False
            while b ** 2 <= i:
                if not dp[i - b**2]:
                    winnable = True
                    break
                b += 1
            dp.append(winnable)
        return dp[-1]
