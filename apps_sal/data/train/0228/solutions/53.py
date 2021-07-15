class Solution:
    def maxVowels(self, s: str, k: int) -> int: 
        _max = 0
        start = 0
        length = 0
        count = 0
        
        for end in range(len(s)):
            length += 1
            
            if self.check(s[end]):
                count += 1
            
            if length > k:
                if self.check(s[start]):
                    count -= 1
                start += 1
                
            _max = max(_max, count)
        
        return _max
                
    
    def check(self, ch):
        vowels = ['a', 'e', 'i', 'o', 'u']
        for vowel in vowels:
            if ch == vowel:
                return True
        
        return False
