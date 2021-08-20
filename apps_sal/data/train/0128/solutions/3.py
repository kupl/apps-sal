class Solution:

    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        res = 0
        sign = 1
        number = 0
        for i in range(len(s)):
            c = s[i]
            if c.isdigit():
                number = number * 10 + int(c)
            elif c == '+':
                res += number * sign
                sign = 1
                number = 0
            elif c == '-':
                res += number * sign
                sign = -1
                number = 0
            elif c == '(':
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
                number = 0
            elif c == ')':
                res += number * sign
                res *= stack.pop()
                res += stack.pop()
                number = 0
                sign = 1
        res += number * sign
        return res
