from collections import Counter
class Solution:
    def reorderedPowerOf2(self, N):
        c = Counter(str(N))
        for i in range(32):
            if Counter(str(1 << i)) == c:
                return True
        return False
