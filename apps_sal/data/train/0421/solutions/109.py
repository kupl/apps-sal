class Solution:
    def lastSubstring(self, s: str) -> str:
        
        c = max(set(s))
        
        res = ''
        
        for i,x in enumerate(s):
            if x == c:
                res = max(res, s[i:])
        return res

