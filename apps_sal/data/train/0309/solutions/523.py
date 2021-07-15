class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        d = {}
        mx = 0
        for i in range(len(A)):
            for j in range(i):
                diff = A[i] - A[j]
                if (diff, i) not in d:
                    d[(diff, i)] = 2
                if (diff, j) in d:
                    d[(diff, i)] = max(d[(diff,i)], d[(diff, j)] + 1)
                mx = max(mx, d[(diff, i)])
        return mx
                    
        
                    
                
        
        
                

