class Solution:

    def isSubsequence(self, s, t):
        if len(s) == 0:
            return True
        if len(s) > len(t):
            return False
        if s[0] not in t:
            return False
        else:
            return self.isSubsequence(s[1:], t[t.index(s[0]) + 1:])
        '\n         :type s: str\n         :type t: str\n         :rtype: bool\n         '
