class Solution:
    def profitableSchemes(self, G: int, P: int, group: List[int], profit: List[int]) -> int:
        mod = int(10**9) + 7
        N = len(group)
        dp = [[[None] * (G + 1) for _ in range(P + 1)] for _ in range(N + 1)]

        def solve(i, j, k):
            if k < 0:
                return 0
            if i == N:
                return 1 if j == 0 else 0
            if dp[i][j][k] is None:
                result = solve(i + 1, j, k) + solve(i + 1, max(j - profit[i], 0), k - group[i])
                dp[i][j][k] = result % mod
            return dp[i][j][k]
        return solve(0, P, G)
