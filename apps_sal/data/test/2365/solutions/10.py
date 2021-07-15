class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        exp=collections.deque(expression)
        
        def or_opt(exp):
            exp.popleft() # skip (
            ret=False
            while exp:
                ret |= exp_opt(exp)
                if exp.popleft()==')': return ret
        
        def and_opt(exp):
            exp.popleft() # skip (
            ret=True
            while exp:
                ret &= exp_opt(exp)
                if exp.popleft()==')': return ret
                                
        def exp_opt(exp):
            ch=exp.popleft()
            ret=False
            if ch=='t': ret=True
            elif ch=='f': ret=False
            elif ch=='!': exp.popleft(); ret=not exp_opt(exp); exp.popleft() # remove (,)
            elif ch=='|': ret=or_opt(exp)
            elif ch=='&': ret=and_opt(exp)
            return ret
        
        return exp_opt(exp)    
