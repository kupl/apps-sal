import math


class Solution:
    squares = [0]
    dp = [False]

    def winnerSquareGame(self, n: int) -> bool:
        sqt = int(math.sqrt(n))
        for i in range(len(self.squares), sqt + 1):
            self.squares.append(i * i)
        if n + 1 <= len(self.dp):
            return self.dp[n]
        old_len = len(self.dp)
        for i in range(old_len, n + 1):
            self.dp.append(False)
        for i in range(old_len, n + 1):
            flag = 0
            for j in range(1, int(math.sqrt(i)) + 1):
                if not self.dp[i - self.squares[j]]:
                    self.dp[i] = True
                    flag = 1
                    break
            if flag == 0:
                self.dp[i] = False
        return self.dp[n]
