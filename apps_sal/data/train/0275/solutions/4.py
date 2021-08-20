class Solution:

    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a = 0
        b = 0
        for i in range(len(s)):
            if s[i] == '*':
                a = a + 1
                if b > 0:
                    b = b - 1
            elif s[i] == '(':
                a = a + 1
                b = b + 1
            elif s[i] == ')':
                a = a - 1
                if b > 0:
                    b = b - 1
            if a < 0:
                return False
        if b == 0:
            return True
        else:
            return False
