class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        import re
        pattern = re.compile(p)
        match = pattern.match(s)
        if match:
            try:
                return match.group() == s
            except:
                return False
            finally:
                pass
        else:
            return False
