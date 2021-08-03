class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        n = len(s)
        if n < minSize:
            return 0
        c = collections.Counter()
        for start in range(n - minSize + 1):
            temp = s[start:start + minSize]
            tc = collections.Counter(temp)
            if len(tc.keys()) <= maxLetters:
                c[temp] += 1
            else:
                continue
            for i in range(start + minSize, min(n, start + maxSize)):
                tc[s[i]] += 1
                temp += s[i]
                if len(tc.keys()) <= maxLetters:
                    c[temp] += 1
                else:
                    continue
        return max(c.values() or [0])
