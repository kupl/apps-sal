class Solution(object):
    def parse(self, expression, d, i):
        count = 0
        start = i
        if expression[i] == "(":
            count += 1
            i += 1
            while count != 0:
                if expression[i] == "(":
                    count += 1
                elif expression[i] == ")":
                    count -= 1
                i += 1
            val = self.evaluate(expression[start:i], d)
        else:
            while i < len(expression) and expression[i] != " " and expression[i] != ")":
                i += 1
            val = expression[start:i]
            if self.isnumber(val):
                val = int(val)
        return i, val

    def get_left_right(self, expression, d):
        i = 0
        count = 0
        i, left = self.parse(expression, d, 0)
        if i == len(expression) or expression[i] == ")":
            return left, None, i
        i += 1
        i, right = self.parse(expression, d, i)
        return left, right, i

    def isnumber(self, s):
        for c in s:
            if ord("0") <= ord(c) <= ord("9") or c == "+" or c == "-":
                continue
            else:
                return False
        return True

    def evaluate(self, expression, d={}):
        """
        :type expression: str
        :rtype: int
        """
        if self.isnumber(expression):
            return int(expression)
        newd = {}
        for key in d:
            newd[key] = d[key]
        expression = expression[1:len(expression) - 1]
        oper = ""
        if expression[0:3] == "add" or expression[:3] == "let":
            oper = expression[0:3]
            expression = expression[4:]
        else:
            oper = "mult"
            expression = expression[5:]

        if oper == "mult" or oper == "add":
            left, right, _ = self.get_left_right(expression, newd)
            if isinstance(left, str):
                left = newd[left]
            if isinstance(right, str):
                right = newd[right]
            if oper == "mult":
                return left * right
            else:
                return left + right
        i = 0
        while True:
            left, right, i = self.get_left_right(expression, newd)
            expression = expression[i + 1:]
            if right == None:
                if isinstance(left, str):
                    return newd[left]
                return left
            if isinstance(right, str):
                right = newd[right]
            newd[left] = right

 # s = Solution()
 # print(s.evaluate("(let x 2 (mult x (let x 3 y 4 (add x y))))"))
