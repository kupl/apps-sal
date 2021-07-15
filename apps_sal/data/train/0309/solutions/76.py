class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        
        if len(A) <= 2:
            return len(A)
        
        n = len(A)
        memo = {}
        
        for i in range(n):
            for j in range(i + 1,n):
                diff = A[j] - A[i]
                memo[(j, diff)] = memo[(i, diff)] + 1 if (i, diff) in memo else 2
        
        return max(memo.values())
