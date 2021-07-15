class Solution:
  def numOfSubarrays(self, arr: List[int]) -> int:
    res, s, prev_odd, prev_even = 0, 0, 0, 1
    for v in arr:
      s = (s + v) % 2
      if s == 1:
        res += prev_even
        prev_odd += 1
      else:
        res += prev_odd
        prev_even += 1
      
    return res % (10**9 + 7)
