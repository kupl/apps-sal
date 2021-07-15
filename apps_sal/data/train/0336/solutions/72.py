class Solution:
    def minSteps(self, s: str, t: str) -> int:
        sdict={}
        for i in s:
            if sdict.get(i) == None:
                sdict[i]=1
            else:
                sdict[i]+=1
        
        for j in t:
            if sdict.get(j):
                sdict[j]-=1
        
        return sum(sdict.values())

