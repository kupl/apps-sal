class Solution:
  # 520 ms
  def longestSubarray(self, nums, limit):
    # initialize maximum and minimum
    _min = _max = nums[0]
    count = 0
    res, start =1, 0

    for right in range(len(nums)):
      # update maximum and minimum
      if _min > nums[right]: _min = nums[right]
      if _max < nums[right]: _max = nums[right]

      # if the right bound valid, count and update result 
      if _max - _min <= limit:
        count += 1
        if res < count: res = count

      # if invalid, turn to find the valid left bound
      elif _max - _min > limit:
        # initialize maximum and minimum at this position
        _min = _max = nums[right]
        count = 1
        left = right - 1
        # keep updating until invalid
        while (left >= start
               and abs(_max - nums[left]) <= limit 
               and abs(_min - nums[left]) <= limit):
          if _min > nums[left]: _min = nums[left]
          if _max < nums[left]: _max = nums[left]
          count += 1
          left -= 1
        # when ended, update the left bound to right+1
        # because we have counted the \"right\" position now in while-loop above already
        start = right + 1

    return res
