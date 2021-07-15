class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        n = len(A)
        if K >= n: return sum(A)
        
        B = [0] * (n+1)
        B[1] = A[0]
        for i in range(1, n):
            B[i+1] = B[i] + A[i]
        
        maxSum = 0
        
        @lru_cache(None)
        def dp(si, ei, remainK):
            if ei == n:
                return (B[ei] - B[si]) / (ei - si)
            tmp = 0 
            if remainK > 1:
                tmp = max(tmp, (B[ei] - B[si]) / (ei - si) + dp(ei, ei+1, remainK - 1))
                
            tmp = max(tmp, dp(si, ei+1, remainK))
            return tmp
            
        #maxSum = max(maxSum, dp(ovr_))
        maxSum = dp(0, 1, K)
        print(maxSum)
        
        return maxSum
