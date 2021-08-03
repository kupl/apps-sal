import numpy as np


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        nums = np.array(nums, dtype=int)
        fullsum = nums.sum() % p
        if fullsum == 0:
            return 0
        # print(fullsum)
        res = np.inf
        indmap = {0: -1}
        for i, a in enumerate(nums.cumsum()):
            subsum = (a - fullsum) % p
            # print(i,a,subsum)
            if subsum in indmap:
                res = min(res, i - indmap[subsum])
                print(res)
            indmap[a % p] = i
        if res == np.inf or res == len(nums):
            return -1

        return res
