class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dir = {}
        res = 0
        for i in range(len(A)):
            
            for j in range(0, i):
                diff = A[i] - A[j]
                if (j, diff) not in dir:
                    dir[(i, diff)] = 2
                else:
                    dir[(i, diff)] = dir[(j, diff)] + 1
                    
                res = max(res, dir[(i, diff)])
        return res
                    

