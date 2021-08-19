class Solution:

    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        i = 0
        lst = []
        while i < len(s):
            for j in range(minSize, maxSize + 1):
                subs = s[i:i + j]
                sc = set(subs)
                if len(sc) > maxLetters:
                    continue
                if len(subs) >= minSize and len(subs) <= maxSize and (i + j <= len(s)):
                    lst.append(subs)
            i += 1
        c = collections.Counter(lst)
        maxs = 0
        for subs2 in c:
            maxs = max(c[subs2], maxs)
        return maxs
