import collections
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        c1=collections.Counter(s)
        c2=collections.Counter(t)
        c=0
        for i in s:
            if c2[i]>0:
                c1[i]-=1
                c2[i]-=1
        l=list(c1.values())
        c=sum(l)
        return c
