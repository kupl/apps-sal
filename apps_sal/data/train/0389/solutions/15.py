class Solution:
    def splitArraySameAverage(self, A: List[int]) -> bool:
        la = len(A)
        sa = sum(A)
       
        memo = {}
        
        def find(target,k,i): # k is needed length, i is the ith element
            if k==0: return target==0
            if k+i>la: return False
         
            if (target,k,i) in memo: return memo[(target,k,i)]
            
            memo[(target,k,i)] = find(target-A[i],k-1,i+1) or find(target,k,i+1)
            return memo[(target,k,i)]
        
        return any(find(j*sa//la,j,0) for j in range(1,la//2+1) if j*sa%la==0)

