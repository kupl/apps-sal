class Solution:

    def winnerSquareGame(self, n: int) -> bool:

        def removeSquare(n: int, memo: [int]):
            if n == 0:
                return False
            if memo[n]:
                return memo[n]
            i = 1
            while i * i <= n:
                if memo[n - i * i] == False:
                    return True
                memo[n - i * i] = removeSquare(n - i * i, memo)
                if memo[n - i * i] == False:
                    return True
                i += 1
            return False
        memo = [None] * (n + 1)
        return removeSquare(n, memo)
