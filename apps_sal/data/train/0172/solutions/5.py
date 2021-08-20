class Solution:

    def maxDiff(self, num: int) -> int:
        s = str(num)
        a = True
        i = 0
        while i < len(s):
            if a and int(s[i]) < 9:
                n = s[i]
                a = False
            if not a:
                if s[i] == n:
                    s = s[:i] + '9' + s[i + 1:]
            i += 1
        n1 = int(s)
        s = str(num)
        a = True
        if int(s[0]) > 1:
            n = s[0]
            y = '1'
            s = y + s[1:]
            a = False
        i = 1
        while i < len(s):
            if a and int(s[i]) > 0:
                if s[i] != s[0]:
                    n = s[i]
                    y = '0'
                    a = False
            if not a:
                if s[i] == n:
                    s = s[:i] + y + s[i + 1:]
            i += 1
        n2 = int(s)
        return n1 - n2
