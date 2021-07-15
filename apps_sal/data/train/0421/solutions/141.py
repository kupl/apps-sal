class Solution:
    def lastSubstring(self, s: str) -> str:
        maxLet = ord(s[0])

        for c in s:
            maxLet = max(maxLet, ord(c))
        
        maxLet = chr(maxLet)
        mx = s
        for i,c in enumerate(s):
            if c == maxLet:
                mx = max(mx,s[i:])
                
        return mx
