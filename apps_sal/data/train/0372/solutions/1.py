class Solution(object):
    def isMatch(self, string, expr):
        self.memo = {(0, 0): True}
        self.string = string
        self.expr = expr
        N = len(string)
        M = len(expr)

        return self.get(N, M)

    def get(self, i, j):
        if i < 0 or j < 0:
            return False

        if (i, j) not in self.memo:
            self.memo[(i, j)] = self.eval(i, j)

        return self.memo[(i, j)]

    def eval(self, i, j):
        if j <= 0:
            return False
        if self.expr[j - 1] == '*':
            prev_char = self.expr[j - 2]

            if prev_char == '.' or i >= 1 and prev_char == self.string[i - 1]:
                if self.get(i - 1, j):
                    return True

            return self.get(i, j - 2)

        else:
            if self.expr[j - 1] == '.' or i >= 1 and self.expr[j - 1] == self.string[i - 1]:
                return self.get(i - 1, j - 1)

            return False
