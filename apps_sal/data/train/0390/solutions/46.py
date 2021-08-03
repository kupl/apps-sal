class Solution:
    def winnerSquareGame(self, n: int) -> bool:

        dp = [False for i in range(n + 1)]

        for num in range(1, n + 1):
            for j in range(1, num + 1):
                if j * j > num:
                    break
                dp[num] = dp[num] or not dp[num - j * j]
                if(dp[num]):
                    break

        print(dp)
        return dp[n]
