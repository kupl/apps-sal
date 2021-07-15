class Solution:

    def get_arg_list(self, s1: List): 
        args = []
        while s1 and isinstance(s1[-1], bool): 
            args.append(s1.pop())
        return args
    
    def boolEval(self, symbol, s1: List):
        if symbol == '!': 
            return not s1[0]
        elif symbol == '&': 
            return all(s1)
        elif symbol == '|': 
            return any(s1)
        else: 
            raise ValueError('Invalid Symbol')
                
    def parseBoolExpr(self, expression: str) -> bool:
        # push ! & | ( onto stack1
        # push t and f onto stack2 
        # pop ( from stack 1 when encounter )
        # if top stack 1 is not paren, then use to evaluate using stack 2
        s1 = []        
        
        for c in expression: 
            if c == '!' or c == '|' or c == '(' or c == '&': 
                s1.append(c)
            elif c == 't' or c == 'f': 
                s1.append(True if c == 't' else False)
            elif c == ')': 
                args = self.get_arg_list(s1)
                s1.pop()
                top = s1[-1]
                while top == '!' or top == '|' or top == '&': 
                    ret = self.boolEval(s1.pop(), args)
                    s1.append(ret)
                    args = self.get_arg_list(s1)
                    top = None if not s1 else s1[-1]
                s1 += args

            elif c == ',': 
                pass
            else: 
                raise ValueError('Invalid character')

        return s1[0]

