import numpy as np


class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        # locs = np.where(np.array(nums) == 1)[0]
        # return np.all(np.diff(locs) > k)
        locs = [i for i in range(len(nums)) if nums[i] == 1]
        return all([locs[i + 1] - locs[i] > k for i in range(len(locs) - 1)])
