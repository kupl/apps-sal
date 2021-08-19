class Solution:

    def winnerSquareGame(self, n: int) -> bool:
        if n == 1 or n == 3 or n == 4 or (n == 6):
            return True
        if n == 0 or n == 2 or n == 5:
            return False
        dp = [0, 1, 0, 1, 1, 0, 1, 0]
        i = 8
        while i <= n:
            j = 1
            add = False
            while j * j <= i:
                if dp[i - j * j] == 0:
                    dp.append(1)
                    add = True
                    break
                j += 1
            if not add:
                dp.append(0)
            i += 1
        return dp[n]
