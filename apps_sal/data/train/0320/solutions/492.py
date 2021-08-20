import numpy as np


class Solution:

    def minOperations(self, nums: List[int]) -> int:
        ops = 0
        arr = np.array(nums)
        while np.sum(arr) != 0:
            inds = np.where(arr % 2 == 1)[0]
            ops += len(inds)
            arr[inds] -= 1
            if np.sum(arr) != 0:
                arr = arr / 2
                ops += 1
        return ops
