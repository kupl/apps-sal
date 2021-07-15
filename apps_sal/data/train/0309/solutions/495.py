class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        if len(A) <= 1:
            return len(A)
        
#         memo = [(1 + 2 * 500) * [1] for _ in range(1 + len(A))]
        
#         res = 0
        
#         for i in range(len(A)-2, -1, -1):
#             for j in range(i+1, len(A)):
#                 diff = A[j] - A[i] + 500
#                 memo[i][diff] = max(memo[i][diff], memo[j][diff] + 1)
#                 res = max(res, memo[i][diff])
        
        h = dict()
        
        res = 0
        
        for i in range(1, len(A)):
            for j in range(i):
                diff = A[j] - A[i]
                h.setdefault((j, diff), 1)
                h[(i, diff)] = h[(j, diff)] + 1
                res = max(res, h[(i, diff)])
    
        return res
