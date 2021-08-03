class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = collections.defaultdict(int)
        for i in range(len(A)):
            for j in range(i):
                dp[(i, A[i] - A[j])] = dp[(j, A[i] - A[j])] + 1
        return max(dp.values()) + 1
