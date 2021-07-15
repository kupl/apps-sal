from typing import List
import numpy

class Solution:
  def constrainedSubsetSum(self, nums: List[int], k: int) -> int:

    _len = len(nums)
    dp = numpy.zeros(_len, dtype=int)
    dp[0] = nums[0]
    _deque = []
    result = -sys.maxsize
    for i in range(_len):

      while _deque and i - _deque[0] > k:
        _deque.pop(0)

      tmp = 0
      if _deque:
        tmp = dp[_deque[0]]
      dp[i] = max(nums[i], nums[i] + tmp)
      result = max(result, dp[i])

      while _deque and dp[i] >= dp[_deque[-1]]:
        _deque.pop()

      _deque.append(i)
      pass


    return result

