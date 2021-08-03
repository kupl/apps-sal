from collections import Counter, defaultdict


class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:

        d = defaultdict(int)
        for i in range(len(s) - minSize + 1):
            sub = s[i:i + minSize]
            if len(Counter(sub)) <= maxLetters:
                d[sub] += 1
        return max(d.values()) if len(list(d.values())) else 0
