class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        # if n == 1:
        #     return True
        # if n == 2:
        #     return False

        dp = [0] * (n + 1)
        # dp[1] = 1

        for i in range(1, n + 1):
            base = 1
            while i - base**2 >= 0:
                if dp[i - base**2] == False:
                    dp[i] = 1
                    break
                base += 1

        return dp[-1]
