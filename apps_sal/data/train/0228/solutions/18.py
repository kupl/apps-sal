class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowelMap = {
            'a': 0,
            'e': 0,
            'i': 0,
            'o': 0,
            'u': 0
        }
        
        for i in range(0, k):
            if s[i] in vowelMap:
                vowelMap[s[i]] += 1
        
        maxVowels = sum(vowelMap.values())
        for i in range(1, len(s)-k+1):
            if s[i+k-1] in vowelMap:
                vowelMap[s[i+k-1]] += 1
            
            if s[i-1] in vowelMap:
                vowelMap[s[i-1]] -= 1
            
            maxVowels = max(maxVowels, sum(vowelMap.values()))
        
        return maxVowels

