import numpy as np


class Solution:

    def nthPersonGetsNthSeat(self, n: int) -> float:
        """
        if n==1:
            currentsum = 0
        else:
            currentsum = 1/n
            for i in range(2,n):
                currentsum = currentsum + currentsum/(n-i+1)
        return 1-currentsum
        """
        if n == 1:
            return 1
        else:
            return 1 / 2.0
