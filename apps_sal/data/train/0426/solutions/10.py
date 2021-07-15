from itertools import permutations

class Solution:
    def reorderedPowerOf2(self, x: int) -> bool:
        n = 1
        pows = set()
        for i in range(31):
            pows.add(n)
            n <<= 1        
        
        for p in permutations(str(x)):
            if p[0] == '0': continue
            if int(''.join(p)) in pows: return True
        
        return False
