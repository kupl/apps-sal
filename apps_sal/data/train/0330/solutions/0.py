class Solution:
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dot = False
        exp = False

        try:
            while s.startswith(' '):
                s = s[1:]
            while s.endswith(' '):
                s = s[:-1]
            if s.startswith('-') or s.startswith('+'):
                s = s[1:]
        except IndexError:
            return False

        if s == '':
            return False

        if s.startswith('e'):
            return False
        if (s[-1] > '9' or s[-1] < '0') and s[-1] != '.':
            return False

        if s.startswith('.'):
            if len(s) == 1:
                return False
            elif s[1] < '0' or s[1] > '9':
                return False

        i = 0
        while i < len(s):
            if s[i] < '0' or s[i] > '9':
                if s[i] == '.':
                    if not dot and not exp:
                        dot = True
                    else:
                        return False
                elif s[i] == 'e':
                    if not exp:
                        exp = True
                        if s[i + 1] == '-' or s[i + 1] == '+':
                            i = i + 1
                    else:
                        return False
                else:
                    return False
            i = i + 1
        return True
