class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        # dp = defaultdict(int)
        dp = {}
        for i in range(1, len(A)):
            for j in range(i):
                diff = A[i] - A[j]
                if (j,diff) in dp:
                    dp[(i,diff)] = dp[(j,diff)] + 1
                else:
                    dp[(i,diff)] = 1
        return max(dp.values()) + 1
