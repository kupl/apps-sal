from collections import defaultdict
class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        
        letdict = defaultdict(int)
        subdict = defaultdict(int)
        uniquecount = 0
        start = end = 0
        n = len(s)
        
        while end < n:
            val = s[end]
            letdict[val] += 1
            if letdict[val] == 1:
                uniquecount += 1
            
            while uniquecount > maxLetters or ((end-start)+1) > maxSize:
                val = s[start]
                letdict[val] -= 1
                if letdict[val] == 0:
                    uniquecount -= 1
                start += 1
                
            tstart = start
            while ((end-tstart)+1) >= minSize:
                subdict[s[tstart:end+1]] += 1
                tstart += 1

            end += 1
        if not subdict:
            return 0
        return subdict[max(subdict, key = lambda x: subdict[x])]
