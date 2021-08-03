import collections
import numpy as np


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        tem = list(zip(position, speed))
        tem = sorted(tem, key=lambda x: x[0])
        count = 0
        stack = [(target - tem[i][0]) / tem[i][1] for i in range(len(tem))]
        stack = stack[::-1]
        cur = 0
        for j in range(len(stack)):
            if stack[j] > cur:
                count += 1
                cur = stack[j]
        return count
