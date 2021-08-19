class Solution:

    def findSubstring(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> str:
        len_s = len(s)
        substrings = {}
        for i in range(len_s):
            for j in range(i + minSize, i + maxSize + 1):
                if j > len_s:
                    break
                substring = s[i:j]
                if len(set(substring)) <= maxLetters:
                    if substring not in substrings:
                        substrings[substring] = 0
                    substrings[substring] += 1
        return substrings

    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        len_s = len(s)
        if len_s < minSize:
            return 0
        substrings = self.findSubstring(s, maxLetters, minSize, maxSize)
        if not substrings:
            return 0
        return max(substrings.values())
