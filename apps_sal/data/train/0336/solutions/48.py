class Solution:
    def minSteps(self, s: str, t: str) -> int:
        #         sdict = collections.defaultdict(int)
        #         tdict = collections.defaultdict(int)
        #         for c in s:
        #             sdict[c] += 1
        #         for c in t:
        #             tdict[c] += 1

        #         res = 0
        #         for c in string.ascii_lowercase:
        #             res += abs(tdict[c] - sdict[c])
        #         return res // 2
        sdict = collections.defaultdict(int)
        for c in s:
            sdict[c] += 1
        for c in t:
            sdict[c] -= 1
        res = 0
        for c in sdict.keys():
            if sdict[c] < 0:
                res += abs(sdict[c])
        return res
