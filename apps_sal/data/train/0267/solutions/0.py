class Solution:

    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        s = []
        for token in tokens:
            if token == '+':
                a = int(s.pop())
                b = int(s.pop())
                s.append(a + b)
            elif token == '/':
                a = int(s.pop())
                b = int(s.pop())
                s.append(b / a)
            elif token == '*':
                a = int(s.pop())
                b = int(s.pop())
                s.append(a * b)
            elif token == '-':
                a = int(s.pop())
                b = int(s.pop())
                s.append(b - a)
            else:
                s.append(token)
        if len(s) is not 1:
            return False
        else:
            return int(s.pop())
