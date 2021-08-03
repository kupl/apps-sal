class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        choices = [1]
        memo = {}
        for i in range(2, n):
            if i * i > n:
                break
            choices.append(i * i)

        def find(n):
            if n == 0:
                return False
            if n in memo:
                return memo[n]
            for i in choices:
                if i > n:
                    break
                if not find(n - i):
                    memo[n] = True
                    return True
            memo[n] = False
            return False
        return find(n)
