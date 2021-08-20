class Solution:

    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        pushed.reverse()
        popped.reverse()
        stack = []
        while pushed:
            stack.append(pushed.pop())
            while stack and popped and (stack[-1] == popped[-1]):
                popped.pop()
                stack.pop()
        if not stack:
            return True
        return False
