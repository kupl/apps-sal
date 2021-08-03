import math


class Solution:
    squares = []

    def winnerSquareGame(self, n: int) -> bool:
        sqt = int(math.sqrt(n))
        for i in range(len(self.squares), sqt + 1):
            self.squares.append(i * i)

        dp = [False] * (n + 1)

        for i in range(1, n + 1):
            flag = 0
            for j in range(1, int(math.sqrt(i)) + 1):
                if not dp[i - self.squares[j]]:
                    dp[i] = True
                    flag = 1
                    break
            if flag == 0:
                dp[i] = False
        print(dp)
        return dp[n]
