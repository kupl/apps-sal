class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        @lru_cache(None)
        def help(A,K):
            n = len(A)
            if K==1:
                return sum(A)
            if K>=n:
                return n*max(A)
            cMax = [A[0]]
            for i in range(1,K):
                cMax.append(max(cMax[-1],A[i]))
            return max((i+1)*cMax[i] + help(A[i+1:],K) for i in range(K))
        return help(tuple(A),K)
            

