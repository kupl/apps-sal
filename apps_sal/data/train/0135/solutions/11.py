class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        if len(pushed) != len(popped): return False
        
        stack, i = [], 0
        
        for j, n in enumerate(pushed):
            stack.append(n)
            while len(stack) > 0 and popped[i] == stack[-1]:
                stack.pop()
                i += 1
                
        return len(stack) == 0

