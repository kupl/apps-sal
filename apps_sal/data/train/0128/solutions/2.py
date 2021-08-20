class Solution:

    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        res = 0
        sign = 1
        stack = [1]
        num = 0
        for c in s:
            if c <= '9' and c >= '0':
                num = num * 10 + ord(c) - ord('0')
            elif c in '+-':
                res += sign * num
                if c == '+':
                    sign = stack[-1]
                else:
                    sign = stack[-1] * -1
                num = 0
            elif c == '(':
                stack.append(sign)
            elif c == ')':
                stack.pop()
        res += sign * num
        return res
