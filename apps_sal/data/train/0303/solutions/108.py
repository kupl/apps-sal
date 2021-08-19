class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        #
        def rec(l, h):
            if h - l < K:
                dp[l][h] = (h - l + 1) * max(A[l:h + 1])
                return dp[l][h]
            m = []
            if dp[l][h] > 0:
                return dp[l][h]
            for i in range(0, K):
                m += [rec(l, l + i) + rec(l + i + 1, h)]
            dp[l][h] = max(m)
            return dp[l][h]

        dp = [0] * len(A)
        dp = [[0] * len(A) for i in range(len(A))]

        rec(0, len(A) - 1)

        return dp[0][len(A) - 1]
