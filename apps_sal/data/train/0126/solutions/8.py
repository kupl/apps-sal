class Solution:

    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        if len(s) < minSize:
            return 0
        occur = {}
        (l, r) = (0, minSize)
        while r <= len(s):
            sub = s[l:r]
            if occur.get(sub) is None:
                distinct = set(sub)
                if len(distinct) <= maxLetters:
                    occur[sub] = 1
            else:
                occur[sub] += 1
            l += 1
            r += 1
        return max(occur.values()) if len(occur) > 0 else 0
