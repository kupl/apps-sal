class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        
        alle = True
        for i in range(1,len(A)):
            if A[i]!=A[i-1]:
                alle = False
                break
                
        if alle:
            return 1

        if len(A)<=2:
            return len(A)
        
        prev = A[0]-A[1]
        maxl = 1
        
        i,j = 0,1
        
        while j < len(A):
            
            
            cur = A[j-1]-A[j]
            #print(j,prev,cur)
            if (cur <=0 and prev <=0) or (cur >=0 and prev >=0):
                #print(j,i)
                ll = j-i
                maxl = max(ll,maxl)
                i = j-1
                
            prev = cur
            j += 1
            
        ll = j-i
        maxl = max(ll,maxl)
        
        return maxl
                
                
                
                 
             
        
        
        
        
        

