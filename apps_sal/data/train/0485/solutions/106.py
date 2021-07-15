class Solution(object):
    def minKBitFlips(self, A, K):
        N=len(A)
        flip=0
        flip_ends=[0]*(N+1)
        res=0
        
        for i,num in enumerate(A):
            flip^=flip_ends[i]
            if not num^flip:
                if i+K>N:
                    return -1
                else:
                    res+=1
                    flip^=1
                    flip_ends[i+K]=1
                
            
        return res
            
      
        
       

