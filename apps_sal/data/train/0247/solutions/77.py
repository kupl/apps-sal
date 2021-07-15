class Solution:
  # 872 ms
  def minSumOfLengths(self, arr, target):
    if len(arr) < 2: return -1
    if arr.count(target) >= 2: return 2
    result = inf = 2**31-1
    i = window = 0
    premin = [inf] * len(arr)

    # i: window start, j: window end
    for j, num in enumerate(arr):
      window += num
      while window > target:
        window -= arr[i]
        i += 1
      if window == target:
        # curr: length
        curr = j - i + 1
        if result > curr + premin[i - 1]:
            result = curr + premin[i - 1]
        premin[j] = curr if curr < premin[j - 1] else premin[j - 1]
        
      else:
        premin[j] = premin[j - 1]

    return result if result < inf else -1
