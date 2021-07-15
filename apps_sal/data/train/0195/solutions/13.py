class Solution:
    def countTriplets(self, A: List[int]) -> int:
        d={}
        for i in A:
            for j in A:
                if(i&j in d):
                    d[i&j]+=1
                else:
                    d[i&j]=1
        c=0
        for i in A:
            for j in d:
                if(i&j==0):
                    c+=d[j]
        return c
            
                
                    
            
                

