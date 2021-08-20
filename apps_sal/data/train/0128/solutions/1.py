class Solution:

    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        (total, tmp, sign) = (0, 0, 1)
        numStack = []
        signStack = []
        for c in s:
            if c == '+':
                (total, tmp, sign) = (total + tmp * sign, 0, 1)
            elif c == '-':
                (total, tmp, sign) = (total + tmp * sign, 0, -1)
            elif c == '(':
                numStack.append(total)
                signStack.append(sign)
                (total, tmp, sign) = (0, 0, 1)
            elif c == ')':
                total += tmp * sign
                (total, tmp, sign) = (total * signStack.pop() + numStack.pop(), 0, 1)
            elif '0' <= c <= '9':
                tmp = tmp * 10 + ord(c) - ord('0')
            else:
                continue
        return total + tmp * sign
