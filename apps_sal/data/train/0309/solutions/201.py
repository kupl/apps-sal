class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        # dp[(index, diff)] equals to the length of arithmetic sequence at index with difference diff.
        dp = collections.defaultdict(int)

        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                dp[(j, A[j] - A[i])] = dp[(i, A[j] - A[i])] + 1

        return max(dp.values()) + 1
