from itertools import permutations

class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        
        # Brute force, check every permutation
        res = False
        for n in permutations(str(N)):
            if n[0] == '0':
                continue
            n = int(''.join(n))
            res = max(res, not (n & (n-1)))
            
        return res
