class Solution:

    def winnerSquareGame(self, n: int) -> bool:
        if n == 1:
            return True
        if n == 2:
            return False
        dp = [0] * n
        dp[0] = True
        dp[1] = False
        count = 2
        for i in range(2, n):
            if i + 1 == count ** 2:
                dp[i] = True
                count += 1
            elif dp[i - 1] == False:
                dp[i] = True
            else:
                cur = 0
                for j in range(count - 1, 1, -1):
                    if dp[i - j ** 2] == False:
                        dp[i] = True
                        cur = 1
                        break
                if cur == 0:
                    dp[i] = False
        return dp[n - 1]
