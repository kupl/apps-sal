class Solution:

    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        cache = collections.defaultdict(int)
        for i in range(len(s) + 1 - minSize):
            if len(set(s[i:i + minSize])) <= maxLetters:
                cache[s[i:i + minSize]] += 1
        res = 0
        for (k, v) in list(cache.items()):
            res = max(res, v)
        return res
