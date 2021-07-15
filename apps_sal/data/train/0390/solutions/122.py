class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        memo = {}
        def isSquare(n):
            root = int(n ** 0.5)
            return root * root == n
        def dfs(n):
            if n in memo:
                return memo[n]
            if isSquare(n):
                memo[n] = True
                return memo[n]
            root = int(n ** 0.5)
            memo[n] = False
            for i in range(1, root + 1):
                if not dfs(n - i * i):
                    memo[n] = True
                    break
            return memo[n]
        return dfs(n)
