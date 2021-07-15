class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        res = 0
        stack = [float('inf')]
        
        for a in arr:
            while stack[-1] <= a:
                m = stack.pop()
                res += m * min(a,stack[-1])
            stack.append(a)
            
        while len(stack) > 2:
            res += stack.pop()*stack[-1]
            
        return res
                

