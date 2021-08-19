class Solution:

    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        (m, n) = (len(A), len(B))
        dp = collections.defaultdict(int)
        for i in range(m):
            for j in range(n):
                match = 1 if A[i] == B[j] else 0
                dp[i, j] = max(dp[i - 1, j - 1] + match, dp[i - 1, j], dp[i, j - 1])
        return dp[m - 1, n - 1]
