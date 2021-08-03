class Solution:
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        try:
            float(s.strip())
            return True
        except:
            return False
