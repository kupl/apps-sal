class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        self.result = 0
        mem = collections.defaultdict()
        n = len(A)
        m = len(B)

        def dfs(pos_a, pos_b):
            if pos_a >= n or pos_b >= m:
                return 0
            if (pos_a, pos_b) in mem:
                return mem[(pos_a, pos_b)]
            best = 0
            for i in range(pos_a, n):
                for j in range(pos_b, m):
                    if A[i] == B[j]:
                        best = max(best, dfs(i + 1, j + 1) + 1)
                    best = max(best, dfs(i + 1, j), dfs(i, j + 1))
            mem[(pos_a, pos_b)] = best
            return best
        dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + 1)
                dp[i][j] = max(dp[i][j], dp[i - 1][j], dp[i][j - 1])
        return dp[-1][-1]
