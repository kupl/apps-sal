class Solution:

    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        r = 0
        seen = Counter()
        for i in range(minSize, maxSize + 1):
            for j in range(i, len(s) + 1):
                t = s[j - i:j]
                if len(set(t)) <= maxLetters:
                    seen[t] += 1
                    if seen[t] > r:
                        r = seen[t]
        return r
