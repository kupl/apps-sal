from collections import defaultdict


class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        N = len(A)
        dp = [defaultdict(lambda: 1) for _ in range(N)]
        for i in range(N):
            for j in range(i + 1, N):
                diff = A[j] - A[i]
                dp[j][diff] = dp[i][diff] + 1
        return max([max(d.values()) for d in dp])
