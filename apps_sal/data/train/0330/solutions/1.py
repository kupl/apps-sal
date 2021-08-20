class Solution:

    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        num = dot = exp = sign = False
        numAfterE = True
        n = len(s)
        for i in range(len(s)):
            if s[i] == ' ':
                if i < n - 1 and s[i + 1] != ' ' and (num or dot or exp or sign):
                    return False
            elif s[i] in '+-':
                if i > 0 and s[i - 1] != 'e' and (s[i - 1] != ' '):
                    return False
                sign = True
            elif s[i].isdigit():
                num = True
                numAfterE = True
            elif s[i] == '.':
                if dot or exp:
                    return False
                dot = True
            elif s[i] == 'e':
                if exp or not num:
                    return False
                exp = True
                numAfterE = False
            else:
                return False
        return num and numAfterE
