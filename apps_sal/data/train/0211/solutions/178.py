class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        N = len(s)
        def splitLookup(ss, used): 
            Ns = len(ss)
            if ss in used: 
                maxSs = 0
            else: 
                maxSs = 1
            i = 1;
            while i < Ns and Ns-i > maxSs - 1: 
                sub = ss[:i]
                if sub not in used: 
                    Nsplit = splitLookup(ss[i:], used | {sub})
                    if Nsplit + 1 > maxSs: 
                        maxSs = Nsplit + 1
                i += 1
            return maxSs
        
        return splitLookup(s, set())

