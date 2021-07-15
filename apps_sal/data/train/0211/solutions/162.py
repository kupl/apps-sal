class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def maxU(s, soFar=set()):
            if len(s) == 1:
                if s in soFar: return 0
            maxSplit = len(soFar)+1
            for partition in range(1, len(s)):
                a = s[:partition]
                b = s[partition:]
                if a not in soFar:
                    maxSplit = max(maxSplit, maxU(b, soFar|{a}))
            return maxSplit
        return maxU(s)

