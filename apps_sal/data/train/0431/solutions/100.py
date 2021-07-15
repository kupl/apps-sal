class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        
        larr=[-1]*len(A)
        rarr=[-1]*len(A)
        
        for i in range(len(A)):
            lefti=i-1
            while lefti>-1 and A[lefti]>A[i]:
                lefti=larr[lefti]-1
                
            larr[i]=lefti+1
            
        
        for i in range(len(A)-1,-1,-1):
            righti=i+1
            
            while righti<len(A) and A[righti]>=A[i]:
                righti=rarr[righti]+1
                
            rarr[i]=righti-1
            
        # print(larr)
        # print(rarr)
            
        count=0
        for i in range(len(A)):
            r,l=rarr[i]-i,i-larr[i]
            count+=((1+l+r+(l*r))*A[i])
            
        return count%(10**9+7)
    
    


