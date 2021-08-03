class Solution:
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        for c in sorted(list(set(s))):
            substr = s[s.index(c):]
            if set(substr) == set(s):
                return c + self.removeDuplicateLetters(substr.replace(c, ""))
        return s
