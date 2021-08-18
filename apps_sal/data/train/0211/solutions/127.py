class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def allsplit(s):
            if len(s) == 1:
                return [[s]]

            res = [[s]]
            for i in range(1, len(s)):
                res += [[s[:i]] + x for x in allsplit(s[i:])]
            return res

        ans = 0

        for sp in allsplit(s):
            if len(sp) == len(set(sp)):
                ans = max(ans, len(sp))
        return ans
