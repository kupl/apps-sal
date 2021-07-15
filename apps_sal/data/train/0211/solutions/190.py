class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def numway(s):
            #if not s: return 0
            nw=0
            for i in range(1,len(s)+1):
                if s[:i] not in nq: 
                    nq.add(s[:i])
                    nw=max(nw,1+numway(s[i:]))
                    nq.remove(s[:i])
            return nw
        nq=set()
        return numway(s)
