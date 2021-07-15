class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        L=arr
        m=0
        t=0
        l=0
        lm=0
        sm=0
        for i in L:
            l+=i
            lm=max(lm,l)
            if(t+i>0): t+=i
            else: t=0
            m=max(m,t)
            sm+=i
        
        r=0
        rm=0
        for i in range(len(L)-1,-1,-1):
            r+=L[i]
            rm=max(rm,r)
            
            
        #print(lm,rm,m)
            
        if(k==1): return m%(10**9+7)
        elif(k==2): return max(m,(rm+lm))%(10**9+7)
        else:
            s=(rm+lm)%(10**9+7)
            if(sm>0):
                return max(m,(s+sm*(k-2)))%(10**9+7)
            else: return max(s,m)%(10**9+7)

