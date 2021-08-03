class Solution:
    def winnerSquareGame(self, n: int) -> bool:

        dp = [False] * (n + 1)

        for i in range(n + 1):
            # we search downwards, alice can win (i.e. = True)
            # only we can take a square number away and hit a dp[False]
            # otherwise it's false

            # if square, we auto win
            if i == int(sqrt(i))**2:
                # print('sq', i)
                dp[i] = True
            else:
                for j in range(1, int(i**0.5) + 1):
                    if not dp[i - j * j]:
                        # print(i, j*j)
                        dp[i] = True
                        break

        # print(dp)
        return dp[n]
