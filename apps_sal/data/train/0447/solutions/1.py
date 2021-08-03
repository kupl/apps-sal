class Solution:
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        chars = set(s)
        for c in sorted(chars):
            suffix = s[s.index(c):]
            if set(suffix) == chars:
                return c + self.removeDuplicateLetters(suffix.replace(c, ''))
        return ''
