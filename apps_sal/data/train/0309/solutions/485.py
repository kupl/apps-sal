from collections import defaultdict


class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        n = len(A)
        dp = [defaultdict(lambda: 1) for _ in range(n)]
        ans = 2
        for i in range(n):
            for j in range(i):
                dp[i][A[i] - A[j]] = max(dp[j][A[i] - A[j]] + 1, 2)
                ans = max(ans, dp[i][A[i] - A[j]])
        return ans
