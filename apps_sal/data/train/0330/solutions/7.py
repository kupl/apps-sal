class Solution:
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        try:
            _ = float(s)
        except:
            return False
        return True
