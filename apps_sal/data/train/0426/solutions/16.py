import itertools
import math


class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        if N == 1:
            return True
        for i in list(itertools.permutations(list(str(N)))):
            if i[0] != '0' and int(i[-1]) % 2 == 0:
                num = int(''.join(i))
                if bin(num).count('1') == 1:
                    return True

        return False
