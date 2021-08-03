import re
import numpy as np


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        nums = np.array(nums)
        zeros_ = np.where(nums == 0)[0]
        if zeros_.tolist():
            temp = []
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
                temp.append(count_ + count__)
            return max(temp)
        elif np.sum(nums) == 0:
            return 0
        else:
            return len(nums) - 1

        # sumnums = sum(nums)
        # if sumnums==len(nums):
        #     return sumnums-1
        # elif sumnums ==0:
        #     return 0
        # elif sumnums == 1:
        #     return 1
        # else:
        #     temp = []
        #     for i in range(len(nums)):
        #         temp1 = [nums[i]]
        #         for j in range(i+1, len(nums)):
        #             if sum(temp1+[nums[j]])>=len(temp1):
        #                 temp1.append(nums[j])
        #             else:
        #                 break
        #         temp.append(temp1)
        #     return max([len(x) for x in temp])-1
