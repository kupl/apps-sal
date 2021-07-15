class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        # O(N ** 2) DP
        dp = {}
        n = len(A)
        for i in range(n):
            for j in range(i + 1, n):
                diff = A[j] - A[i]
                dp[(j, diff)] = dp.get((i, diff), 1) + 1
        return max(dp.values())
