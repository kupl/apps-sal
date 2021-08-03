import itertools
import math


class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        for i in list(itertools.permutations(list(str(N)))):
            if i[0] != '0':  # and int(i[-1]) % 2 == 0
                num = int(''.join(i))
                # print('i ', i)
                # print('num ', num)
                # print('round(math.log2(num)) ', round(math.log2(num)))
                # print('math.log2(num) ', math.log2(num))
                if round(math.log2(num)) == math.log2(num):
                    # print(i)
                    # print(num)
                    return True

        return False
