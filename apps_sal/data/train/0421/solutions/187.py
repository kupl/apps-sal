class Solution:
    def lastSubstring(self, s: str) -> str:
        maxs = None
        for sidx in range(len(s)):
            if maxs == None or s[sidx:] > maxs:
                maxs = s[sidx:]
        return maxs
