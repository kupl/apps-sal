class Solution:

    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        n = len(pushed)
        i = j = 0
        while True:
            if not stack or stack[-1] != popped[j]:
                if i >= n:
                    return not stack
                stack.append(pushed[i])
                i += 1
            else:
                stack.pop()
                j += 1
