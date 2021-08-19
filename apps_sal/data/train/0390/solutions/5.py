class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        # 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30
        # t f t t f t f t t f  t  f  t  t  f  t  f  t  t  f  t  f  t  t  t  t  t  t  t  t

        if n == 1:
            return True
        if n == 2:
            return False

        dp = [0] * n
        dp[0] = True
        dp[1] = False
        count = 2

        for i in range(2, n):
            if (i + 1) == count ** 2:
                dp[i] = True
                count += 1
            else:
                if dp[i - 1] == False:
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
