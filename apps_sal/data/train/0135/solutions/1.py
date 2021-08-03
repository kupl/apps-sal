class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        if len(pushed) != len(popped):
            return False
        idx = 0
        stack = []
        for i in range(len(popped)):
            if len(stack) > 0 and stack[-1] == popped[i]:
                stack.pop()
            else:
                while idx < len(pushed) and pushed[idx] != popped[i]:
                    stack.append(pushed[idx])
                    idx += 1
                idx += 1
        return len(stack) == 0
