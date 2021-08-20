class Solution:

    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        cnt = Counter()
        res = collections.Counter()
        size = minSize
        while size <= maxSize:
            for i in range(len(s) - size + 1):
                ss = s[i:i + size]
                if len(set(ss)) <= maxLetters:
                    res[ss] += 1
            size += 1
        return max(res.values()) if res else 0
