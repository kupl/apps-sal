class Solution:

    def winnerSquareGame(self, n: int) -> bool:
        if int(n ** 0.5) ** 2 == n:
            return True
        sqdict = {i * i: 1 for i in range(1, n + 1)}
        dp = [False for i in range(n + 1)]
        dp[:4] = [False, True, False, True]
        for i in range(4, n + 1):
            if sqdict.get(i, 0) == 1:
                dp[i] = True
            else:
                for j in sqdict:
                    if j > i:
                        break
                    if dp[i - j] == False:
                        dp[i] = True
                        break
        return dp[n]
