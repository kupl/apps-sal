class Solution:
    def helper(self,B,s,e,d):
        
        if len(B)==0:
            d[(s,e)]=0
            return 0
            
        if (s,e) in d:
            return d[(s,e)]
        
        
        cost=e-s
        m=2**31-1
        for i in range(len(B)):
            m=min(m,self.helper(B[:i],s,B[i],d)+self.helper(B[i+1:],B[i],e,d))
            
        d[(s,e)]=cost+m
        
        return cost+m
    
    def minCost(self, n: int, cuts: List[int]) -> int:
       
        cuts.sort()
        d={}
        k=self.helper(cuts,0,n,d)
        return k

