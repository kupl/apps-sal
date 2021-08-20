class Solution:

    def isSubsequence(self, s, t):
        t = iter(t)
        return all((c in t for c in s))

    def isSubsequenceFei(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        (p, l) = (0, len(s))
        if l == p:
            return True
        for c_t in t:
            if s[p] == c_t:
                p += 1
            if p == l:
                return True
        return False
