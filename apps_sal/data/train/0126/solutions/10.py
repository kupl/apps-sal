class Solution:

    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        res = collections.Counter()
        b = 0
        cc = collections.Counter()
        for e in range(len(s)):
            cc[s[e]] += 1
            while len(cc) > maxLetters or e - b + 1 > maxSize:
                cc[s[b]] -= 1
                if cc[s[b]] == 0:
                    cc.pop(s[b])
                b += 1
            i = b
            while e - i + 1 >= minSize:
                res[s[i:e + 1]] += 1
                i += 1
        return res.most_common(1)[0][1] if res else 0
