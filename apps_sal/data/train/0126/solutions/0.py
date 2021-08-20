class Solution:

    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        n = len(s)
        count = collections.Counter((s[i:i + minSize] for i in range(0, n - minSize + 1)))
        res = 0
        for (k, v) in count.items():
            if len(set(k)) <= maxLetters:
                res = max(res, v)
        return res
