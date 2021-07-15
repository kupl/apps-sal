import numpy as np
class Solution:
    def minOperations(self, n: int) -> int:
        res = np.zeros((n,1),dtype=int)
        for i in range(n):
            value = 2*i+1-n
            if value>0:
                res[i] = value
        return res.sum()
