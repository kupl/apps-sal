class Solution:
    def numSplits(self, s: str) -> int:
        res = 0

        # construct dict from 1 to last
        # iterate from 1 and remove the elm from dict (if 0 then del elm from dict) and add it to the set
        # check if leng are equal
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
