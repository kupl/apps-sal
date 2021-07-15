import numpy as np
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        n = len(arr)
        dict_model = {}
        for it in arr:
            if it in dict_model.keys():
                dict_model[it] += 1
            else:
                dict_model[it] = 1
        min_deactivate = np.ceil(n/2)
        generators = list(dict_model.values())
        generators.sort()
        turn_off = 0
        i = 1
        while turn_off < min_deactivate:
            turn_off += generators[-i]
            i += 1
        return i-1
