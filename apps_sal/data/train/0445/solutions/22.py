
import copy
from typing import List
import numpy

import sys
# Definition for a binary tree node.
# Definition for a binary tree node.
class Solution:
  def minDifference(self, nums: List[int]) -> int:
    result = 0

    if len(nums) <= 4:
      return 0

    nums.sort()
    result = sys.maxsize
    result = min(result, nums[-1] - nums[3])
    result = min(result, nums[-2] - nums[2])
    result = min(result, nums[-3] - nums[1])
    result = min(result, nums[-4] - nums[0])
    return result


