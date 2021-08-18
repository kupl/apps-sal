import numpy as np


class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()

        sums = []
        temp = [0] * len(satisfaction)
        for i in range(len(satisfaction), 0, -1):
            temp = np.add(temp, [0] * (i - 1) + satisfaction[i - 1:])
            sums.append(np.sum(temp))

        result = max(sums)
        return result if result > 0 else 0
