class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = {}
        
        for i in range(len(A)):
            for j in range(i):
                d = A[j] - A[i]
                if (j, d) in dp:
                    dp[(i, d)] = dp[(j, d)] + 1
                else: 
                    dp[(i, d)] = 2
                    
        return max(dp.values())
