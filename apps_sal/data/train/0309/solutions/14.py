class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        
        from collections import defaultdict

        d = [{} for _ in range(len(A))]
        res = 2

        for i, x in enumerate(A):
            for j in range(i):
                diff = x - A[j]
                if diff in d[j]:
                    d[i][diff] = d[j][diff] + 1
                    # d[j].pop(diff)
                    
                    res = max(res, d[i][diff])
                    
                else:
                    d[i][diff] = 2

                
        return res


