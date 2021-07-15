from itertools import accumulate

class Solution:
  def countTriplets(self, nums: List[int]) -> int:
    n, x = len(nums), list(accumulate(nums, lambda x, y: x ^ y, initial=0))
    count = 0
    for i in range(1, n + 1 - 1):
      for j in range(i + 1, n + 1):
        for k in range(j + 0, n + 1):
          if x[i - 1] ^ x[j - 1] == x[j - 1] ^ x[k]:
            count += 1
    return count
