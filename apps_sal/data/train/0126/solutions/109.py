from collections import Counter

class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        substrings = {}
        for i in range(len(s)-minSize+1):
            sub = s[i:i+minSize]
            if sub in substrings:
                substrings[sub] += 1
            else:
                if len(Counter(sub)) <= maxLetters:
                    substrings[sub] = 1
        if len(substrings):
            return max(substrings.values())
        else:
            return 0
