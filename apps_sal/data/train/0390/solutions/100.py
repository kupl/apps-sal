class Solution:

    def winnerSquareGame(self, n: int) -> bool:
        if n == 1:
            return True
        dp = [0, 1]
        for i in range(2, n + 1):
            root = int(i ** 0.5)
            if root ** 2 == i:
                dp.append(1)
            else:
                for j in range(1, root + 1):
                    if not dp[i - j ** 2]:
                        dp.append(1)
                        break
            if len(dp) == i:
                dp.append(0)
        return dp[n]
