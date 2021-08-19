class Solution:
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        open = 0
        star = 0
        count = {'(': 0, ')': 0, '*': 0}
        newS = []
        for i in s:
            #count[i] += 1
            if i == ')':
                if open > 0:
                    open -= 1
                    del newS[len(newS) - 1 - newS[::-1].index('(')]
                elif star > 0:
                    star -= 1
                    del newS[len(newS) - 1 - newS[::-1].index('*')]
                else:
                    return False
            elif i == '(':
                open += 1
                newS += '('
            else:
                star += 1
                newS += '*'

        if star >= open:
            o = 0
            s = 0
            for i in newS:
                if i == '(':
                    o += 1
                elif i == '*':
                    if o > 0:
                        o -= 1

            if o != 0:
                return False
            else:
                return True
        else:
            return False
