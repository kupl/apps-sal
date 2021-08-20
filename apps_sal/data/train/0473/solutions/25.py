import numpy as np


class Solution:

    def countTriplets(self, arr: List[int]) -> int:
        cumxor = [arr[0]]
        for k in range(1, len(arr)):
            cumxor.append(cumxor[-1] ^ arr[k])
        counter = 0
        for x in range(1, len(arr)):
            if cumxor[x] == 0:
                counter += x
            for y in range(x):
                if cumxor[x] == cumxor[y]:
                    counter += x - y - 1
        return counter
