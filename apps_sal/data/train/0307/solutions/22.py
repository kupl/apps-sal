class Solution:
    def soupServings(self, N: int) -> float:
        # 5:02 10/4/20

        def dfs(a, b):
            if a <= 0 and b <= 0:
                return 0.5
            if a <= 0 and b > 0:
                return 1
            if a > 0 and b <= 0:
                return 0
            if memo[a][b] != -1:
                return memo[a][b]
            memo[a][b] = 0.25 * (dfs(a - 4, b) + dfs(a - 3, b - 1) + dfs(a - 2, b - 2) + dfs(a - 1, b - 3))
            return memo[a][b]
        if N >= 5000:
            return 1
        n = N // 25 + int(N % 25 > 0)
        memo = [[-1] * 200 for _ in range(200)]
        return dfs(n, n)
