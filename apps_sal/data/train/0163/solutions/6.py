class Solution:
    def isSubsequence(self, s, t):
        t = iter(t)
        return all(c in t for c in s)
