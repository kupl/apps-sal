class Solution:

    def maxUniqueSplit(self, s: str) -> int:
        c = collections.Counter(s)
        res = len(c.keys())
        l = len(s)
        ways = int(math.pow(2, l - 1))
        for i in range(ways):
            bit = str(bin(i))[2:].zfill(l - 1)
            cand = [s[0]]
            for (i, x) in enumerate(bit):
                if x == '0':
                    cand[-1] += s[i + 1]
                else:
                    cand.append(s[i + 1])
            nodup = set(cand)
            if len(nodup) == len(cand):
                res = max(res, len(cand))
        return res
