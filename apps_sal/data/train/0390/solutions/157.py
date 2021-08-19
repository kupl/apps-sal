class Solution:

    def winnerSquareGame(self, n: int) -> bool:
        memo = {}

        def f(x):
            if x == 0:
                return False
            if x == 1:
                return True
            if x in memo:
                return memo[x]
            i = 1
            while i * i <= x:
                if f(x - i * i) == False:
                    memo[x] = True
                    return True
                i += 1
            memo[x] = False
            return False
        return f(n)
