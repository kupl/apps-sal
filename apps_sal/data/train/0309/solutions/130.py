class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = {}
        L = len(A)
        for i in range(L):
            for j in range(i):
                diff = A[i] - A[j]
                dp[(i, diff)] = dp.get((j, diff), 1) + 1
        
        return max(dp.values())
