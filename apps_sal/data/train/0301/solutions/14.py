class Solution:

    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        dp = collections.defaultdict(int)
        (m, n) = (len(A), len(B))
        for x in range(m):
            for y in range(n):
                cur = 0
                if A[x] == B[y]:
                    cur = 1
                dp[x, y] = max(dp[x - 1, y - 1] + cur, dp[x - 1, y], dp[x, y - 1])
        return dp[m - 1, n - 1]
