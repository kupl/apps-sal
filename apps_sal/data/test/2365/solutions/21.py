import operator
from typing import List


class Solution:

    @staticmethod
    def split_by_comma(expression: str) -> List[str]:
        start = 0
        bracket_balance = 0
        answer = []
        for i in range(len(expression)):
            if expression[i] == '(':
                bracket_balance += 1
            if expression[i] == ')':
                bracket_balance -= 1
            if expression[i] == ',' and (not bracket_balance):
                answer.append(expression[start:i + 1])
                start = i + 1
        answer.append(expression[start:])
        return answer

    def parseBoolExpr(self, expression: str) -> bool:
        if expression.startswith('t'):
            return True
        if expression.startswith('f'):
            return False
        if expression.startswith('!'):
            return not self.parseBoolExpr(expression[2:-1])
        if expression.startswith('|'):
            return any(map(self.parseBoolExpr, self.split_by_comma(expression[2:-1])))
        else:
            return all(map(self.parseBoolExpr, self.split_by_comma(expression[2:-1])))
