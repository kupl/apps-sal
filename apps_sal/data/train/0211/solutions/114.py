class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def split(s):
            if len(s) == 0:
                return []
            if len(s) == 1:
                return [[s]]
            res = []
            for i in range(1,len(s) + 1):
                ans = [s[:i]]
                splits = split(s[i:])
                if splits:
                    for sub in splits:
                        res.append(ans + sub)
                else:
                    res.append(ans)
            return res
        
            
        options = split(s)
        m = 0
        for o in options:
            if len(o) == len(set(o)):
                m = max(m, len(o))
        return m
