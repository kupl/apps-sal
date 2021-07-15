class Solution:
  def minOperations(self, nums: List[int]) -> int:
    cost = 0
    d = 0
    for a in nums:
      division, increments = self.trick(a)
      d = max(division, d)
      cost += increments
    return d + cost
  
  def trick(self, mx):
    if mx in {0, 1}:
      return (0, 0) if mx == 0 else (0, 1)
    if mx % 2 == 0:
      d, i = self.trick(mx // 2)
      return (d + 1, i)
    else:
      d, i = self.trick(mx - 1)
      return (d, i + 1)

