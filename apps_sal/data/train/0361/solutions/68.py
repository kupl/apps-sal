class Solution:

    def tilingRectangle(self, n: int, m: int) -> int:
        self.best = m * n
        height = [0] * m

        def dfs(moves):
            if all((h == n for h in height)):
                self.best = min(self.best, moves)
                return
            if moves >= self.best:
                return
            idx = height.index(min(height))
            for i in range(min(m - idx, n - height[idx]), 0, -1):
                for j in range(i):
                    height[idx + j] += i
                dfs(moves + 1)
                for j in range(i):
                    height[idx + j] -= i
        dfs(0)
        return self.best
        '\n    # dp + cheating\n    def tilingRectangle(self, n: int, m: int) -> int:\n        if (m, n) in {(11, 13), (13, 11)}: return 6\n        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]\n        self.helper(m, n, dp)\n\n        return dp[m][n]\n\n    def helper(self, m, n, dp):\n        horizontalMin = sys.maxsize\n        verticalMin = sys.maxsize\n        if m == n:\n            dp[m][n] = 1\n            return dp[m][n]\n        if dp[m][n] != 0:\n            return dp[m][n]\n        for i in range(1, m // 2 + 1):\n            horizontalMin = min(self.helper(m - i, n, dp) + self.helper(i, n, dp), horizontalMin)\n        for j in range(1, n // 2 + 1):\n            verticalMin = min(self.helper(m, n - j, dp) + self.helper(m, j, dp), verticalMin)\n        dp[m][n] = min(horizontalMin, verticalMin)\n\n        return dp[m][n]\n        '
