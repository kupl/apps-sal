class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        from collections import defaultdict, Counter
        d = defaultdict(int)
        for i in range(len(s)-minSize+1):
            t = s[i:i+minSize]
            if len(Counter(t)) <= maxLetters:
                d[t] += 1
        return max(d.values()) if d else 0

