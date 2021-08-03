import bisect


class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:

        dp = {}

        for i, num in enumerate(A):
            for j in range(i + 1, len(A)):
                diff = A[j] - num
                if (i, diff) not in dp:
                    dp[(j, diff)] = 2
                else:
                    dp[(j, diff)] = dp[(i, diff)] + 1

        return max(dp.values())
