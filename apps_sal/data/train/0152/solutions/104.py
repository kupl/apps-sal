class Solution:
  def maxDistance(self, position: List[int], m: int) -> int:
    position.sort()
    def getCount(d: int) -> int:
      last, count = position[0], 1
      for x in position:
        if x - last >= d:
          last = x
          count += 1
      return count
    l, r = 0, position[-1] - position[0] + 1
    t = r
    while l < r:
      mid = l + (r - l) // 2
      if getCount(t - mid) >= m:
        r = mid
      else:
        l = mid + 1
    return t - l
