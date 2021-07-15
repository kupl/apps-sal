from collections import Counter
class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        curr = 1
        N = str(N)
        while len(str(curr)) <= len(N):
            if len(str(curr)) == len(N):
                if Counter(str(curr)) == Counter(str(N)):
                    return True
            curr *= 2
        return False
