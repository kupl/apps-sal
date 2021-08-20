from collections import defaultdict


class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = defaultdict(lambda: 1)
        for (i, a) in enumerate(A):
            for j in range(i):
                diff = A[i] - A[j]
                if dp[i, diff] < dp[j, diff] + 1:
                    dp[i, diff] = dp[j, diff] + 1
        return max(dp.values())
