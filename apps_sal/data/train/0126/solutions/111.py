class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        substrings = dict()
        for i in range(minSize - 1, maxSize):
            for j in range(i,len(s)):
                if len(set(s[j-i: j + 1])) <= maxLetters:
                    substrings[s[j-i: j + 1]] = substrings.get(s[j-i:j + 1], 0) + 1
        return max(substrings.values()) if len(substrings) else 0
