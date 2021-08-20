class Solution:

    def calculate(self, s):
        result = number = 0
        sign = 1
        stack = []
        for i in s:
            if i == ' ':
                continue
            if i.isdigit():
                number = number * 10 + int(i)
            elif i == '+':
                result += sign * number
                number = 0
                sign = 1
            elif i == '-':
                result += sign * number
                number = 0
                sign = -1
            elif i == '(':
                stack.append(result)
                stack.append(sign)
                result = 0
                number = 0
                sign = 1
            elif i == ')':
                result += sign * number
                number = 0
                sign = 1
                result = result * stack.pop() + stack.pop()
        result += number * sign
        return result
