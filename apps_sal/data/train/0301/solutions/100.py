class Solution:

    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        dp = collections.defaultdict(int)
        for i in range(len(A)):
            for j in range(len(B)):
                dp[i, j] = max(dp[i - 1, j - 1] + (A[i] == B[j]), dp[i - 1, j], dp[i, j - 1])
        return dp[len(A) - 1, len(B) - 1]
