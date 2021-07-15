class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        current = 0
        maxx = 0
        start, end = 0, 0
        if k == 0:
            return 0 
        while end < min(start + k, len(s)):
            if s[end] in vowels:
                current += 1
            end += 1
        
        if end == len(s):
            return current
        
        while end < len(s):
            maxx = max(maxx, current)
            if s[start] in vowels:
                current -= 1
            start += 1
            if s[end] in vowels:
                current += 1
            end += 1
            
        return max(maxx, current)
