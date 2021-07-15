class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = {}
        for i in range(1, len(A)):
            for j in range(i):
                diff = A[i]-A[j]
                dp[(i, diff)] = max(dp.get((i, diff), 2), dp.get((j, diff), 1)+1)

        
        # print(dp)
        return max(dp.values())
