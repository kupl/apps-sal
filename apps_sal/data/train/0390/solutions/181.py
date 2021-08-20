class Solution:

    def winnerSquareGame(self, n: int) -> bool:
        memo = {}
        memo[0] = False
        memo[1] = True

        def dfs(n) -> bool:
            if n in memo:
                return memo[n]
            i = 1
            while i * i <= n:
                res = dfs(n - i * i)
                if not res:
                    memo[n] = True
                    return True
                i += 1
            memo[n] = False
            return False
        return dfs(n)
