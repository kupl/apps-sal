class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        memo = {}
        def dfs(n):
            if n == 0:
                return False
            if n in memo:
                return memo[n]
            can_win = False
            for i in range(1, int(n ** 0.5) + 1):
                if not dfs(n - i ** 2):
                    can_win = True
                    break
            memo[n] = can_win
            return memo[n]
        return dfs(n)
