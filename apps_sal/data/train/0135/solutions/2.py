class Solution:

    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        i = 0
        j = 0
        demo = []
        for j in range(len(popped)):
            while popped[j] not in demo and i < len(pushed):
                demo.append(pushed[i])
                i += 1
            if demo[-1] == popped[j]:
                demo.pop()
            else:
                return False
        return True
