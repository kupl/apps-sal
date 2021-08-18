class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        from collections import Counter, defaultdict

        min_val = min(A)
        max_val = max(A)

        global_best = -1
        dp = {}

        for i, v in enumerate(A):
            dp[i] = {}

            for j, w in enumerate(A[:i]):
                d = v - w
                dp[i][d] = dp[j].get(d, 1) + 1
                global_best = max(global_best, dp[i][d])

        return global_best
