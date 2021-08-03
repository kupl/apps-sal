class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = {}

        for i in range(len(A)):
            for j in range(i):
                step = A[i] - A[j]
                dp[(i, step)] = dp.get((j, step), 1) + 1

        return max(dp.values())
