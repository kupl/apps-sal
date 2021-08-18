from typing import List
import numpy

import sys


class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.insert(0, 0)
        horizontalCuts.append(h)
        horizontalCuts.sort()

        verticalCuts.insert(0, 0)
        verticalCuts.append(w)
        verticalCuts.sort()

        maxh = -1
        maxv = -1

        for index, value in enumerate(horizontalCuts):
            if index == 0:
                continue
            maxh = max(maxh, value - horizontalCuts[index - 1])

        for index, value in enumerate(verticalCuts):
            if index == 0:
                continue
            maxv = max(maxv, value - verticalCuts[index - 1])

        module = int(pow(10, 9) + 7)
        result = maxv * maxh % module
        return result
