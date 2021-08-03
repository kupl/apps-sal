class Solution:
    def numPermsDISequence(self, S: str) -> int:
        MOD = 10**9 + 7
        N = len(S)

        dp = [[0] * (N + 1) for _ in range(N + 1)]

        def solve(i, j):
            if not (0 <= j <= i):
                return 0

            if dp[i][j]:
                return dp[i][j]

            if i == 0:
                return 1
            if S[i - 1] == 'D':
                dp[i][j] = (solve(i, j - 1) + solve(i - 1, j - 1)) % MOD
            else:
                dp[i][j] = (solve(i, j + 1) + solve(i - 1, j)) % MOD

            return dp[i][j]

        return sum(solve(N, j) for j in range(N + 1)) % MOD
