class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
      res = 0
      csum = [0]
      for n in nums:
        csum.append(csum[-1]+n)
      # print (csum[1:])
      # print ([c-target for c in csum[1:]])
      seen = set([])
      for c in csum[:]:
        # print (c, c-target, seen)
        if c-target in seen:
          res += 1
          seen.clear()
        seen.add(c)
        
      return res
