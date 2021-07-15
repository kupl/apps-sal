from collections import Counter
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        x = dict(Counter(list(s)))
        count = 0
        for i in range(len(t)):
            v = x.get(t[i],None)
            if(v!=None and v>0):
                x[t[i]]-=1
            else:
                count+=1
        print(count)
        return count
