class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        # dp[(idx, diff)]: length of arithmetic sequence at index with difference diff.
        dp = {}
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                diff = A[j] - A[i]
                dp[(j, diff)] = dp.get((i, diff), 1) + 1
        return max(dp.values())
