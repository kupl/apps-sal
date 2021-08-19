import math
from itertools import permutations


class Solution:

    def permutations2(self, N: int) -> List[int]:
        nums = [''.join(p) for p in permutations(str(N))]
        return [int(n) for n in nums if not n.startswith('0')]

    def reorderedPowerOf2(self, N: int) -> bool:
        permutations = self.permutations2(N)
        for permutation in permutations:
            if math.log2(permutation).is_integer():
                return True
        return False
