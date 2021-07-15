class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        index = {}
        for i in range(len(A)):
            index[A[i]] = i
        record = {}
        
        def dp(i,j):
            if (i,j) in record:
                return record[(i,j)]
            if A[i] + A[j] in index:
                res = 1 + dp(j, index[A[i]+A[j]])
                record[(i,j)] = res
                return res
            else:
                return 2
        
        res = 0
        for i in range(len(A)-1):
            for j in range(i+1, len(A)):
                res = max(res, dp(i,j))
        if res >= 3:
            return res
        else:
            return 0
