from collections import defaultdict


class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        n = len(A)
        if n < 3:
            return n

        dp = defaultdict(lambda: defaultdict(int))
        res = 2
        for i in range(1, n):
            for j in range(i):
                gap = A[i] - A[j]
                dp[i][gap] = max(dp[j][gap] + 1, 2)
                res = max(res, dp[i][gap])
        return res
