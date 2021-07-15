from collections import defaultdict

class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        # mapping: 
        d = defaultdict(lambda: defaultdict(lambda: 1))
        
        for i,a in enumerate(A):
            d[i][0] = 1
            for j in range(i):
                step = A[i] - A[j]
                d[i][step] = d[j][step] + 1
        return max([max(dn.values()) for dn in d.values()])
