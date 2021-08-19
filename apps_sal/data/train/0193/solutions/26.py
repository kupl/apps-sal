import numpy as np
import collections


class Solution:

    def minSetSize(self, arr: List[int]) -> int:
        dict_gens = collections.Counter(arr)
        generators = sorted(dict_gens.values())
        min_deactivate = np.ceil(len(arr) / 2)
        turn_off = 0
        i = 1
        while turn_off < min_deactivate:
            turn_off += generators[-i]
            i += 1
        return i - 1
