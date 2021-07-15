class Solution:
    def lastSubstring(self, s: str) -> str:
        i, j, k = 0, 1, 0
        
        while j + k < len(s):
            if s[i+k] == s[j+k]:
                k += 1
                continue
            elif s[i + k] > s[j + k]:
                j = j + 1
            elif s[i + k] < s[j + k]:
                i = i + 1
            if i == j:
                j = j + 1
            k = 0
            
        
        return s[i:]

