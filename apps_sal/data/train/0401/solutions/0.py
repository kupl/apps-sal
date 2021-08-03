# 5:09
'''
nums = [3,6,5,1,8]
sum_nums = 23
mod3_sum_nums = 2
mod3_dict = {0:[3,6], 1:[1], 2:[5,8]}
helper([5,8], [1]) -> 5





'''

from collections import defaultdict


class Solution:
    def helper(self, l1, l2):
        if len(l1) < 1 and len(l2) < 2:
            sum_remove = 0
        elif len(l1) < 1:
            sum_remove = min(l2)
            l2.remove(sum_remove)
            sum_remove += min(l2)

        elif len(l2) < 2:
            sum_remove = min(l1)

        else:
            sum_remove1 = min(l1)
            sum_remove2 = min(l2)
            l2.remove(sum_remove2)
            sum_remove2 += min(l2)
            sum_remove = min(sum_remove1, sum_remove2)

        return sum_remove

    def maxSumDivThree(self, nums: List[int]) -> int:
        sum_nums = sum(nums)
        mod3_sum_nums = sum_nums % 3
        if mod3_sum_nums == 0:
            return sum_nums

        mod3_dict = defaultdict(list)
        for i, num in enumerate(nums):
            mod3_dict[num % 3].append(num)

        if mod3_sum_nums == 1:
            sum_remove = self.helper(mod3_dict[1], mod3_dict[2])

        else:
            sum_remove = self.helper(mod3_dict[2], mod3_dict[1])

        if sum_remove > 0:
            return sum_nums - sum_remove
        else:
            return 0
