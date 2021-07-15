class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        
        i=0
        maxL = []
        maxM = []
        maxSum = 0
        
        while i<=len(A)-L:
            maxL.append(sum(A[i:i+L]))
            i+=1
            
        i = 0
        while i<=len(A)-M:
            maxM.append(sum(A[i:i+M]))
            i+=1

        for i,elem in enumerate(maxL):
            if i-M<=0:
                prefix = []
            else:
                prefix = maxM[0:i-M]
            
            if len(maxM[i+L:]+prefix)== 0:
                continue
            maxSum = max(maxSum,elem+max(prefix+maxM[i+L:]))
        
        return maxSum        
