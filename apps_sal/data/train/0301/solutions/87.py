class Solution:

    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        (dp, n, m) = (defaultdict(int), len(A), len(B))
        for (a, b) in product(range(n), range(m)):
            dp[a, b] = max(dp[a - 1, b - 1] + (A[a] == B[b]), dp[a - 1, b], dp[a, b - 1])
        return dp[n - 1, m - 1]
