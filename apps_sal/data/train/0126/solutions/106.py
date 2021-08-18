class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        n = len(s)
        d = {}
        for i in range(n):
            for j in range(minSize, maxSize + 1):
                if i + j > n:
                    break
                if len(set(s[i:i + j])) <= maxLetters:
                    d[s[i:i + j]] = d.get(s[i:i + j], 0) + 1
        return max(list(d.values()), default=0)
