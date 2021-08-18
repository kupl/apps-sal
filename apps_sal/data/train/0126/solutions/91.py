from collections import defaultdict


class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        d = defaultdict(int)
        n = len(s)

        for i in range(n):
            for j in range(i + minSize - 1, min(i + maxSize, n)):
                if len(set(s[i:j + 1])) <= maxLetters:
                    d[s[i:j + 1]] += 1
        if d:
            return max(d.values())
        return 0
