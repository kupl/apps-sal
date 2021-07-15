class Solution:
    def numTriplets(self, a1: List[int], a2: List[int]) -> int:
        d={}
        n1=len(a1)
        n2=len(a2)
        for i in range(n1):
            for j in range(i+1,n1):
                if a1[i]*a1[j] in list(d.keys()):
                    d[a1[i]*a1[j]]+=1
                else:
                    d[a1[i]*a1[j]]=1
        c=0
        for x in a2:
            if x*x in list(d.keys()):
                c+=d[x*x]
        e={}
        for i in range(n2):
            for j in range(i+1,n2):
                if a2[i]*a2[j] in list(e.keys()):
                    e[a2[i]*a2[j]]+=1 
                else:
                    e[a2[i]*a2[j]]=1 
        
        for x in a1:
            if x*x in list(e.keys()):
                c+=e[x*x]
        
        return c
            

