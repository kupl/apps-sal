class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        
        counterSubstring = collections.defaultdict(int)
        best = 0
        for start in range(len(s)):
            #for size in range(minSize, maxSize + 1):
            if start + minSize <= len(s):
                substring = s[start:start + minSize]
                counterSubstring[substring] += 1
        
        for substring in counterSubstring:
            if len(set(substring)) <= maxLetters:
                best = max(best, counterSubstring[substring])
        
        return best      
