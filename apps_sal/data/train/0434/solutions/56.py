import re
import numpy as np


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        nums = np.array(nums)
        zeros_ = np.where(nums == 0)[0]
        if zeros_.tolist():
            temp = 0
            for ind in zeros_:
                ind_ = max([ind - 1, 0])
                ind__ = min([ind + 1, len(nums) - 1])
                count_ = 0
                count__ = 0
                if nums[ind_] == 1:
                    while ind_ >= 0 and nums[ind_] == 1:
                        count_ += 1
                        ind_ -= 1
                if nums[ind__] == 1:
                    while ind__ < len(nums) and nums[ind__] == 1:
                        count__ += 1
                        ind__ += 1
                temp = max([count_ + count__, temp])
            return temp
        elif len(zeros_) == len(nums):
            return 0
        else:
            return len(nums) - 1
