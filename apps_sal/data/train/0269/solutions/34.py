import numpy as np


class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        locs = [i for i in range(len(nums)) if nums[i] == 1]
        return all([locs[i + 1] - locs[i] > k for i in range(len(locs) - 1)])
