from collections import Counter


class Solution:

    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        if len(s) < minSize or maxSize == 0:
            return 0
        start = 0
        end = start + minSize
        count = Counter()
        while end <= len(s):
            unique = Counter(s[start:end])
            if len(unique) <= maxLetters:
                count[s[start:end]] += 1
            start += 1
            end += 1
        return max(count.values()) if count else 0
