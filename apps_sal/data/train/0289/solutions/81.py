class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        n = len(A)
        
        prefix = [0] * (n + 1)
        
        for i in range(n):
            prefix[i+1] = prefix[i] + A[i]
            
        maxi = float('-inf')
        for startL in range(n-L+1):
            endL = startL + L - 1
            sumL = prefix[endL+1] - prefix[startL]
            
            for startM in range(startL+1-M):
                endM = startM + M - 1
                sumM = prefix[endM+1] - prefix[startM]
                maxi = max(maxi, sumL + sumM)
                
            for startM in range(endL+1, n-M+1):
                endM = startM + M - 1
                sumM = prefix[endM+1] - prefix[startM]
                maxi = max(maxi, sumL + sumM)
                
        
        return maxi
