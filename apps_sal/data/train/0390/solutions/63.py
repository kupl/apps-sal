from math import floor, sqrt


class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [0 for _ in range(n + 1)]
        for i in range(1, floor(sqrt(n)) + 1):
            dp[i * i] = 1
            great = 1
        for i in range(2, n + 1):
            if dp[i] == 0:
                for j in range(1, great + 1):
                    res = (dp[j * j] + dp[i - j * j]) % 2
                    if res == 1:
                        dp[i] = 1
                        break
            else:
                great += 1
        print(dp)
        return True if dp[n] else False
