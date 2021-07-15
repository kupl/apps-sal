class Solution:
    def lastSubstring(self, s: str) -> str:
        if len(s) == 1:
            return s
        
        start, end, length = 0, 1, 0
        
        while end + length < len(s):
            if s[start + length] == s[end + length]:
                length += 1
            elif s[start + length] > s[end + length]:
                end += length + 1
                length = 0
            else:
                start = end
                end = start + 1
                length = 0
        
        return s[start:]
                

