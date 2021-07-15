class Solution:
    def maxTurbulenceSize(self, A):
        
        ans = 0 
        cnt = 0
        
        for i in range(len(A)):
            
            if i >= 2 and (A[i-2]<A[i-1]>A[i] or A[i-2]>A[i-1]<A[i] ):
                cnt += 1
            elif i >=1 and A[i-1] != A[i]:
                cnt = 2
            else:
                cnt = 1
                
            ans = max(ans,cnt)
            
        return ans
