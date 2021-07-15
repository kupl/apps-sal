class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        push = []
        i = 0
        while popped:
            if i < len(pushed):
                push += [pushed[i]]
            while push and push[-1] == popped[0]:
                popped.pop(0)
                push.pop()
            # print(push)
            # print(popped)
            if i < len(pushed):
                i += 1
            else:
                return False
        return True
