class Solution:
    def numSplits(self, s: str) -> int:
        res = 0

        fs = set()

        d = {}
        for x in s:
            if x not in d:
                d[x] = 1
            else:
                d[x] += 1

        i = 0
        while i < len(s):
            fs.add(s[i])

            if d[s[i]] > 1:
                d[s[i]] -= 1
            else:
                del d[s[i]]

            if len(fs) == len(set(d.keys())):
                res += 1

            i += 1
        return res
