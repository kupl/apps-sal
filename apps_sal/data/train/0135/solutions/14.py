class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        
        stack = []
        push_index = 0
        pop_index = 0
        n = len(pushed)
        
        while push_index < n:
            
            while stack and stack[-1] == popped[pop_index]:
                stack.pop()
                pop_index += 1
            
            stack.append(pushed[push_index])
            push_index += 1
            
            while stack and stack[-1] == popped[pop_index]:
                stack.pop()
                pop_index += 1
        
        return True if not stack else False

