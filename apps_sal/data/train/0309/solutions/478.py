
class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        def helper():
            return 1

        dp = defaultdict(helper)
        for i in range(len(A)):
            for j in range(i):
                step = A[i] - A[j]
                dp[(i, step)] = max(dp[(j, step)] + 1, dp[(i, step)])
        return max(dp.values())

