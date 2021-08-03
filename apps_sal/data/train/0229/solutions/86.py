from collections import Counter
from typing import List


class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        d = dict()
        num_zeros = 0
        for x in A:
            if x == 0:
                num_zeros += 1
                continue
            x = abs(x)
            y = x
            while y % 2 == 0:
                y //= 2
            if y in d:
                d[y].update([x])
            else:
                d[y] = Counter([x])

        if num_zeros % 2:
            return False

        for base, counter in d.items():
            keys = sorted(counter)
            for key in keys:
                if counter[key] <= counter[2 * key]:
                    counter[2 * key] -= counter[key]
                    counter[key] -= counter[key]
                else:
                    return False
        return True
