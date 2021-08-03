class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = {}
        for i in range(1, len(A)):
            for j in range(i):
                delta = A[i] - A[j]
                if (j, delta) in dp:
                    dp[(i, delta)] = dp[(j, delta)] + 1
                else:
                    dp[(i, delta)] = 2
        return max(dp.values())
