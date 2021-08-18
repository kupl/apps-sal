import itertools
import math


class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        for i in list(itertools.permutations(list(str(N)))):
            if i[0] != '0':
                num = int(''.join(i))
                if round(math.log2(num)) == math.log2(num):
                    return True

        return False
