from collections import Counter
class Solution:
    def numSplits(self, s: str) -> int:
        no = 0
        x=Counter(s)
        y=Counter()
        if len(list(x.keys()))==len(list(y.keys())):
            no+=1
        for i in range(0,len(s)-1):
            
            x[s[i]]-=1
            if x[s[i]]==0:
                del x[s[i]]
            if s[i] in y:
                y[s[i]] += 1
            else:
                y[s[i]]=1
                
            if len(list(x.keys())) == len(list(y.keys())):
                no+=1
            
            
            
                
        return no
                

