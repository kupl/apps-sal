import collections
import numpy as np

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if len(position) < 1:
            return 0
        # d = dict(zip(target - np.array(position), speed))
        ord_d = collections.OrderedDict(sorted(dict(zip(target - np.array(position), speed)).items()))
        count = 0
        r = -1
        for dist, speed in ord_d.items():
            t = dist / speed
            if t > r:
                count += 1
                r = t
        return count 
