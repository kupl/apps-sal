class Solution:

    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        l = len(pushed)
        i = 0
        j = 0
        while i < l and j < l:
            if pushed[i] == popped[j]:
                pushed[i] = -1
                popped[j] = -1
                while i > 0:
                    if pushed[i] != -1:
                        break
                    i -= 1
                j += 1
            else:
                i += 1
        i = 0
        j = 0
        r_pop = popped[::-1]
        while i < l and j < l:
            if pushed[i] == -1:
                i += 1
                continue
            if r_pop[j] == -1:
                j += 1
                continue
            if pushed[i] != popped[j]:
                return False
            else:
                i += 1
                j += 1
        return True
