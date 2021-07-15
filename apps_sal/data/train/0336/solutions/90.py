from collections import Counter
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        d1=Counter()
        d2=Counter()
        n=len(s)
        cnt=0
        for i,a in enumerate(s):
            d1[a]=d1[a]+1
        print(d1)
        for j,b in enumerate(t):
            d2[b]=d2[b]+1
        print(d2)
        for k1,v1 in list(d1.items()) :
            if k1 in d2:
                v2=d2[k1]
                cnt=cnt+min(v1,v2)
            
        return n-cnt
            
        

