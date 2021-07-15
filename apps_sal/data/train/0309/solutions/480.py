class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        # longest length with end index i and diff j
        if not A:
            return 0
        
        dp = {}
        n = len(A)
        
        max_len = 0
        
        for j in range(1, n):
            for i in range(0, j):
                if (i, A[j] - A[i]) in dp:
                    dp[(j, A[j] - A[i])] = dp[(i, A[j] - A[i])] + 1
                else:
                    dp[(j, A[j] - A[i])] = 2
                
                max_len = max(max_len, dp[(j, A[j] - A[i])])
                
        return max_len
                
        
                    
                

