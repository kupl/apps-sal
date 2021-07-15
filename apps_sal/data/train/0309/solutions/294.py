class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = {}
        n = len(A)
        
        res = 0
        for r in range(1, n):
            for l in range(r):
                diff = A[r] - A[l]
                
                if (diff, l) in dp:
                    dp[(diff, r)] = dp[(diff, l)] + 1
                    res = max(res, dp[(diff, l)] + 1)
                else:
                    dp[(diff,r)] = 2
                    res = max(res, 2)
        return res
                

