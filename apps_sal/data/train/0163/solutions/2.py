class Solution:
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        length = len(s)
        idx = 0
        for i in range(length):
            idx = t.find(s[i], idx)
            if idx == -1:
                return False
            idx += 1
        return True
