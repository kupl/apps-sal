class Solution:
    def lastSubstring(self, s: str) -> str:
        
        c = max(s)

        i = s.find(c)
        r = i
        
        while i < len(s):
            
            if s[i] == c:
                if s[r:] < s[i:]:
                    r = i
                while i < len(s)-1 and s[i+1] == c:
                    i += 1
                    
            i += 1

        return s[r:]
