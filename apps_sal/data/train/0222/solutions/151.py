class Solution:

    def lenLongestFibSubseq(self, A: List[int]) -> int:
        n = len(A)
        check = set(A)
        dp = {}

        def helper(i, j):
            if (i, j) in dp:
                return dp[i, j]
            total = i + j
            if total not in check:
                result = 2
            else:
                val = helper(j, total)
                result = val + 1
            dp[i, j] = result
            return result
        for i in range(n):
            for j in range(i + 1, n):
                helper(A[i], A[j])
        result = max(dp.values())
        return result if result > 2 else 0
