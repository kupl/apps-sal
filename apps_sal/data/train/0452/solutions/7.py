class Solution:
    def minDifficulty(self, A: List[int], d: int) -> int:
        n = len(A)

        if d > n:
            return -1

        dp = [[math.inf] * (d + 1) for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(1, d + 1):
                if n - i < j:
                    continue
                rMax = -math.inf
                for k in range(i, n - j + 1):
                    rMax = max(rMax, A[k])
                    if j == 1:
                        dp[i][j] = rMax
                    else:
                        dp[i][j] = min(dp[i][j], rMax + dp[k + 1][j - 1])
        return dp[0][d]
