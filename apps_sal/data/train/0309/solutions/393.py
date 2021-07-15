class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = {}
        n = len(A)
        for i in range(n):
            for j in range(i+1,n):
                diff = A[i]-A[j]
                dp[(diff, j)] = dp.get((diff,i), 1) + 1
        #print(dp)
        return max(dp.values())
