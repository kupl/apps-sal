class Solution:

    def isSubsequence(self, s, t):
        iterator = iter(t)
        return all((character in iterator for character in s))
