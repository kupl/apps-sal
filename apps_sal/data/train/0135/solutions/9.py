class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        '''
        start: 1:27
        
        edge cases:
            not poping entire stack (nm, pushed is a permutation of popped)
            
        complexity:
            O(n) time, O(1) space seems right
            
        approach:
            Let's just build a stack and attempt to pop at each opportunity... Seems simple
            Greedy approach, always pop if possible, should work fine due to distinct numbers
        '''
        
        stack = []
        
        while len(pushed) or len(popped) or len(stack):
            if len(stack) and len(popped) and stack[-1] == popped[0]: # can pop
                stack.pop()
                popped = popped[1:]
            elif len(pushed): # can push
                stack.append(pushed[0])
                pushed = pushed[1:]
            else:
                return False
        return True

