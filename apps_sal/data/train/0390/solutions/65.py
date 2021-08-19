class Solution:

    def winnerSquareGame(self, n: int) -> bool:
        dp = [False]
        for i in range(1, n + 1):
            for b in range(1, math.floor(math.sqrt(i)) + 1):
                if not dp[i - b ** 2]:
                    dp.append(True)
                    break
            else:
                dp.append(False)
        return dp[-1]
