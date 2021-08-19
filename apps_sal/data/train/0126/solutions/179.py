from collections import Counter


class Solution:

    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        i = 0
        j = 0
        letterCounts = Counter()
        substrCounts = Counter()
        while j < len(s):
            letterCounts[s[j]] += 1
            while len(letterCounts) > maxLetters or j - i + 1 > minSize:
                letterCounts[s[i]] -= 1
                if letterCounts[s[i]] == 0:
                    del letterCounts[s[i]]
                i += 1
            if j - i + 1 == minSize:
                substrCounts[s[i:j + 1]] += 1
            j += 1
        return 0 if len(substrCounts) == 0 else max(substrCounts.values())
