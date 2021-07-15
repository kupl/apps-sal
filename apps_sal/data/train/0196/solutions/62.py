class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        if len(A) == 0:
            return 0
        minS = minT = maxS = maxT = s = A[0]
        for i in range(1,len(A)):
            minS = min(A[i],minS + A[i])
            minT = min(minS,minT)
            
            maxS = max(A[i],maxS + A[i])
            maxT = max(maxT,maxS)
            
            s += A[i]
        if s == minT:
            return maxT
        return max(s - minT,maxT)
