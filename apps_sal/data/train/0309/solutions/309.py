from collections import defaultdict


class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = [defaultdict(lambda: 1) for _ in range(len(A))]
        for i, a in enumerate(A):
            for j in range(i):
                diff = A[i] - A[j]
                dp[i][diff] = max(dp[i][diff], dp[j][diff] + 1)
        return max(max(lens.values()) for lens in dp)
