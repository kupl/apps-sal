class Solution:

    def winnerSquareGame(self, n: int) -> bool:
        memo = {0: False}

        def dp(i):
            if i in memo:
                return memo[i]
            m = int(i ** 0.5)
            if i ** 0.5 == m:
                return True
            res = False
            for j in range(1, m + 1):
                res |= not dp(i - j * j)
                if res:
                    memo[i] = True
                    return True
            memo[i] = False
            return False
        return dp(n)
