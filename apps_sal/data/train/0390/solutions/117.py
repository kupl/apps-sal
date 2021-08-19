class Solution:
    def winnerSquareGame(self, n: int) -> bool:

        dp = {0: False}

        for i in range(1, n + 1):

            # get dp[i]
            for j in range(1, int(i ** 0.5) + 1):
                sn = j ** 2
                if not dp[i - sn]:
                    dp[i] = True
                    break
            else:
                dp[i] = False

        return dp[n]
