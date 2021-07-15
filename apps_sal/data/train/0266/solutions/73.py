class Solution:
    def numSplits(self, s: str) -> int:
        c=Counter(s)
        d=dict()
        r=0
        for i in s:
            d[i]=1
            if(i in c):
                c[i]-=1
            if(c[i]==0):
                del c[i]
            if(len(c)==len(d)):
                r+=1
        return r
                
                    
        

