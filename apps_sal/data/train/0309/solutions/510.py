class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = {}
        globalMax = 1
        for i, a1 in enumerate(A):
            for j, a2 in enumerate(A[:i]):
                x = a1 - a2
                if (j,x) in dp:
                    dp[(i,x)] = dp[(j,x)] + 1
                else:
                    dp[(i,x)] = 2
                globalMax = max(globalMax, dp[(i,x)])
        return globalMax
