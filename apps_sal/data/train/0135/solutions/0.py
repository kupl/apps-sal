class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        j = 0
        l = []
        for i in pushed:
            l.append(i)
            while l and (l[-1] == popped[j]):
                l.pop()
                j += 1
        if l:
            return False
        return True
