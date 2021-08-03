class Solution:
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # remove whitespaces
        s = s.strip()

        try:
            value = float(s)
            return True
        except:
            return False
