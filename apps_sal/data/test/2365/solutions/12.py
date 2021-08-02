class Solution:
    def parseBoolExpr(self, expression: str) -> bool:

        def split_into_list(expression):

            res = []
            depth = 0
            ss = ''

            for e in expression:
                if depth == 0 and e == ',':
                    res.append(ss)
                    ss = ''

                else:
                    if e == '(':
                        depth += 1
                    elif e == ')':
                        depth -= 1

                    ss += e

            res.append(ss)

            return res

        if expression == 't':
            return True
        if expression == 'f':
            return False

        if expression[0] == '!':
            return not self.parseBoolExpr(expression[2:-1])

        if expression[0] == '&':

            res = True
            for L in split_into_list(expression[2:-1]):
                res &= self.parseBoolExpr(L)

            return res

        if expression[0] == '|':

            res = False
            for L in split_into_list(expression[2:-1]):
                res |= self.parseBoolExpr(L)

            return res
