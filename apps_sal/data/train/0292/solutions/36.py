class Solution:
    def maxAbsValExpr(self, A: List[int], B: List[int]) -> int:
        n = len(A)
        
        max1 = max2 = max3 = max4 = -10**6 - 1 
        min1 = min2 = min3 = min4 = 10**6 + 1
        for i in range(n):
            temp = A[i] - B[i] - i
            min1 = min(min1,temp)
            max1 = max(max1,temp)
            
            temp = A[i] + B[i] - i
            min2 = min(min2,temp)
            max2 = max(max2,temp)
                       
            temp = A[i] + B[i] + i
            min3 = min(min3,temp)
            max3 = max(max3,temp)
            
            temp = A[i] - B[i] +i
            min4 = min(min4,temp)
            max4 = max(max4,temp)
        
        ans = max(max4 - min4, max3 - min3, max2 - min2, max1 - min1)

        return ans
