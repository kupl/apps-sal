class Solution:

    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        pop_index = 0
        length = len(pushed)
        for i in range(length):
            stack.append(pushed[i])
            while stack[-1] == popped[pop_index]:
                print(stack)
                stack.pop()
                pop_index += 1
                if pop_index >= length or len(stack) == 0:
                    break
                continue
        if len(stack) != 0:
            return False
        else:
            return True
