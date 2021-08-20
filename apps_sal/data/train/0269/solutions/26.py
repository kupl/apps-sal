import numpy as np


class Solution:

    def kLengthApart(self, nums: List[int], k: int) -> bool:
        locs = np.where(np.array(nums) == 1)[0]
        return np.all(np.abs(np.diff(locs)) > k)
