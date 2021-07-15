class Solution:
    def countTriplets(self, A: List[int]) -> int:
        d={}
        ans=0
        for i in range(len(A)):
            for j in range(len(A)):
                a=A[i]&A[j]
                d[a]=d.get(a,0)+1
        
        for i in range(len(A)):
            for j in list(d.keys()):
                if A[i]&j==0:
                    ans+=d[j]
        return ans
                    
        
        
        
        
        
        
        

