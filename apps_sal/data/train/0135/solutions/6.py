class Solution:

    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        l = []
        j = i = 0
        for i in pushed:
            l.append(i)
            while l and popped and (l[-1] == popped[0]):
                l.pop()
                popped.pop(0)
        return len(popped) == 0
