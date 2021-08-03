class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        res = 0
        dp = collections.defaultdict(lambda: 1)

        for i in range(len(A) - 1, -1, -1):
            for j in range(i + 1, len(A)):
                dist = A[j] - A[i]
                dp[(i, dist)] = max(dp[(i, dist)], dp[(j, dist)] + 1)

        return max(dp.values())
