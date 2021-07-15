class Solution:
    def lastSubstring(self, s: str) -> str:
        n = len(s)
        
        maxLetter = max(s)
        maxSubstring = None
        
        for i, letter in enumerate(s):
            if letter == maxLetter:
                if not maxSubstring or s[i:n] > maxSubstring:
                    maxSubstring = s[i:n]
        
        return maxSubstring

